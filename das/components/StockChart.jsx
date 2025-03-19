import {LineChart, Line, XAxis, YAxis, Tooltip} from "recharts";
import {useEffect, useState} from "react";


function StockChart({ code, updated }) {
    const [data, setData] = useState([])

    useEffect(() => {
        fetch(`http://localhost:8000/api/table/?code=${code}`)
            .then((response) => response.json())
            .then((fetched_data) => {
                // console.log(fetched_data)
                setData(fetched_data)
            })
            .catch((error) => console.error("Error fetching data:", error));
    }, [code, updated]);

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