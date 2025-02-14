import './App.css'
import SearchBar from "../components/SearchBar.jsx";
import StockChart from "../components/StockChart.jsx";
import StockTable from "../components/StockTable.jsx";

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-blue-600 text-white p-4">
        <h1 className="text-2xl font-bold">Stock Analysis Dashboard</h1>
      </header>
      <main className="p-6">
        <SearchBar />
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
          <StockChart />
          <StockTable />
        </div>
      </main>
    </div>
  );
}

export default App
