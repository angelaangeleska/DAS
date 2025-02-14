import { LineChart, Line, XAxis, YAxis, Tooltip } from "recharts";

const data = [
  { date: "2025-02-10", price: 120 },
  { date: "2025-02-11", price: 125 },
  { date: "2025-02-12", price: 130 },
];

function StockChart() {
  return (
    <div className="p-4 bg-white shadow rounded-md">
      <h2 className="text-lg font-bold mb-4">Stock Price Over Time</h2>
      <LineChart width={400} height={200} data={data}>
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="price" stroke="#8884d8" />
      </LineChart>
    </div>
  );
}

export default StockChart