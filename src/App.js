import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/")  // Request to Flask backend
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.error("Error:", error));
  }, []);

  return (
    <div>
      <h1>Flask says:</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
