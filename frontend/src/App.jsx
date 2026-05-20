import React, { useState } from 'react'

const API_BASE = 'http://localhost:8000'

export default function App() {
  const [name, setName] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

  async function handleSubmit(e) {
    e.preventDefault()
    setLoading(true)
    setResult(null)
    try {
      const res = await fetch(`${API_BASE}/api/player`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name }),
      })
      if (!res.ok) throw new Error(await res.text())
      const data = await res.json()
      setResult(data)
    } catch (err) {
      setResult({ error: err.message })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{ padding: 20, fontFamily: 'system-ui, Arial' }}>
      <h1>NBA Comparer</h1>
      <form onSubmit={handleSubmit} style={{ marginBottom: 12 }}>
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="LeBron James"
          style={{ padding: 8, width: 300 }}
        />
        <button style={{ marginLeft: 8, padding: '8px 12px' }} disabled={loading}>
          Analyze
        </button>
      </form>

      {loading && <p>Loading...</p>}

      {result && result.error && <pre style={{ color: 'red' }}>{result.error}</pre>}

      {result && !result.error && (
        <div>
          <h2>{result.name}</h2>
          <pre style={{ whiteSpace: 'pre-wrap', background: '#f6f6f6', padding: 12 }}>{result.report}</pre>
        </div>
      )}
    </div>
  )
}
