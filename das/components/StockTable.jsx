function StockTable() {
  const stocks = [
    { symbol: "AAPL", name: "Apple Inc.", price: "$150", change: "+1.5%" },
    { symbol: "GOOGL", name: "Alphabet Inc.", price: "$2800", change: "-0.8%" },
  ];

  return (
    <div className="p-4 bg-white shadow rounded-md">
      <h2 className="text-lg font-bold mb-4">Stock Details</h2>
      <table className="w-full text-left border-collapse">
        <thead>
          <tr>
            <th className="border-b p-2">Symbol</th>
            <th className="border-b p-2">Company</th>
            <th className="border-b p-2">Price</th>
            <th className="border-b p-2">Change</th>
          </tr>
        </thead>
        <tbody>
          {stocks.map((stock) => (
            <tr key={stock.symbol}>
              <td className="border-b p-2">{stock.symbol}</td>
              <td className="border-b p-2">{stock.name}</td>
              <td className="border-b p-2">{stock.price}</td>
              <td className={`border-b p-2 ${stock.change.startsWith("+") ? "text-green-500" : "text-red-500"}`}>
                {stock.change}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default StockTable