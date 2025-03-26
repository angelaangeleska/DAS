import { useEffect, useState } from "react";

function CodeDropdown({ setCode }) {
  const [codes, setCodes] = useState([]);
  const [selectedCode, setSelectedCode] = useState(() => {
    return localStorage.getItem('selectedStockCode') || "ABT";
  });

  useEffect(() => {
    fetch("http://localhost:8000/api/codes/")
      .then((response) => response.json())
      .then((data) => setCodes(data))
      .catch((error) => console.error("Error fetching codes:", error));
  }, []);

  const handleChange = (e) => {
    const newCode = e.target.value;
    setSelectedCode(newCode);
    localStorage.setItem('selectedStockCode', newCode);
    setCode(newCode);
  };

  return (
    <select
      value={selectedCode}
      onChange={handleChange}
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
