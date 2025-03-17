import { useEffect, useState } from "react";

function CodeDropdown({ setCode }) {
  const [codes, setCodes] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/codes/")
      .then((response) => response.json())
      .then((data) => setCodes(data))
      .catch((error) => console.error("Error fetching codes:", error));
  }, []);

  return (
    <select
      onChange={(e) => setCode(e.target.value)}
      className="w-full p-2 border rounded-md"
    >
      <option value="ABT">ABT</option>
      {codes.slice(0,30).map((code) => (
        <option key={code} value={code}>
          {code}
        </option>
      ))}
    </select>
  );
}

export default CodeDropdown;
