import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "../pages/Home.jsx";
import Companies from "../pages/Companies.jsx";
import About from "../pages/About.jsx";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-200 flex flex-col">
        {/* Header */}
        <header className="bg-blue-700 text-white p-4 flex items-center shadow-md">
          {/* Logo on the left */}
          <h1 className="text-2xl font-bold flex-1">📈 Stock Analysis </h1>

          {/* Centered Navigation */}
          <nav className="flex space-x-4 mx-auto">
            <Link
              to="/stock"
              className="text-white px-6 py-2 rounded-md shadow-md hover:bg-blue-500 transition"
            >
              Stocks
            </Link>
            <Link
              to="/about"
              className="text-white px-6 py-2 rounded-md shadow-md hover:bg-blue-500 transition"
            >
              About
            </Link>
          </nav>
        </header>

        {/* Main Content */}
        <main className="flex-grow p-6">

          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/stock" element={<Companies />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </main>

        {/* Footer */}
        <footer className="bg-blue-700 text-white text-center p-4 mt-6">
          <p>© 2025 Stock Analysis | Built for DAS with React, Django, Apache Kafka, Apache Spark and Postgres</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
