import {LineChart, Line, XAxis, YAxis, Tooltip} from "recharts";
import {useEffect, useState} from "react";


function StockChart({ code, updated, n=2000 }) {
    const [data, setData] = useState([])

    useEffect(() => {
    // Add cache-busting timestamp parameter
    const fetchUrl = `http://localhost:8000/api/table/?code=${code}&_=${Date.now()}`;

    fetch(fetchUrl)
      .then((response) => response.json())
      .then((fetched_data) => {
        const sortedData = fetched_data.sort((a, b) =>
          new Date(b.date) - new Date(a.date)
        );
        const recentData = sortedData.slice(0, n);
        setData(recentData.reverse());
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, [code, updated, n]); // Dependency array ensures refresh when any of these change

    return (
        <div className="p-4 bg-white shadow rounded-md">
            <h2 className="text-lg font-bold mb-4">Stock Price Over Time</h2>
            <div className="p-4 w-full h-[50vh]">
                <LineChart width={1150} height={390} data={data}>
                <XAxis dataKey="date"/>
                <YAxis/>
                <Tooltip/>
                <Line type="monotone" dataKey="price" stroke="#8884d8"/>
            </LineChart>
            </div>
        </div>
    );
}

export default StockChart