import { useState } from "react";
import "./App.css";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";
type Patient = { id: string; name: string; age: number; condition: string };

function App() {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [rows, setRows] = useState<Patient[]>([]);
  const [error, setError] = useState<string | null>(null);

  const run = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch("http://127.0.0.1:8000/nlq", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });
      const data = await res.json();
      if (!res.ok) {
        if (data?.detail) {
          throw new Error(data.detail);
        }
        throw new Error(`Backend error: ${res.status}`);
      }

      setRows(data.rows ?? []);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : "Unknown error");
      setRows([]);
    } finally {
      setLoading(false);
    }
  };

  // --- Build chart data: count patients by condition ---
  const chartData = Object.values(
    rows.reduce<Record<string, { condition: string; count: number }>>(
      (acc, r) => {
        const key = r.condition || "unknown";
        if (!acc[key]) acc[key] = { condition: key, count: 0 };
        acc[key].count += 1;
        return acc;
      },
      {}
    )
  );

  return (
    <div className="container">
      <h1>AI on FHIR — NLQ Demo</h1>
      <div style={{ display: "flex", gap: 8 }}>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder='e.g. "show diabetic patients over 50"'
          style={{ width: "100%", padding: 8 }}
        />
        <button onClick={run} disabled={loading || !query.trim()}>
          {loading ? "Running..." : "Go"}
        </button>
      </div>

      {error && <p style={{ color: "red" }}>Error: {error}</p>}

      {rows.length > 0 && (
        <>
          <h2>Patients</h2>
          <table border={1} cellPadding={6} style={{ width: "100%" }}>
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Age</th>
                <th>Condition</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((r) => (
                <tr key={r.id}>
                  <td>{r.id}</td>
                  <td>{r.name}</td>
                  <td>{r.age}</td>
                  <td>{r.condition}</td>
                </tr>
              ))}
            </tbody>
          </table>

          {/* --- Chart: Patients per condition --- */}
          <h2 style={{ marginTop: 24 }}>Patients per condition</h2>
          <div style={{ width: "100%", height: 320 }}>
            <ResponsiveContainer>
              <BarChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="condition" />
                <YAxis allowDecimals={false} />
                <Tooltip />
                <Bar dataKey="count" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
