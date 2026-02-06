import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [response, setResponse] = useState(null);

  const sendTest = async () => {
    const res = await fetch("http://localhost:8000/test", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        test: "Hello from react",
        number: 42
      })
    });

    const data = await res.json();
    setResponse(data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Frontend → Backend Test</h1>

      <button onClick={sendTest}>
        Send Test Request
      </button>

      {response && (
        <pre>{JSON.stringify(response, null, 2)}</pre>
      )}
    </div>
  );
}

export default App
