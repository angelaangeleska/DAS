function About() {
  return (
    <div className="bg-white p-8 rounded-lg shadow-lg max-w-4xl mx-auto">
      {/* Introduction Section */}
      <div className="bg-gradient-to-r from-blue-50 to-purple-50 p-6 rounded-lg shadow-md mb-8">
        <h2 className="text-3xl font-bold text-center mb-4 text-gray-800">Introduction</h2>
        <p className="text-lg text-gray-700 bg-white p-4 rounded-lg shadow-sm">
          Our stock analysis dashboard is designed to provide you with comprehensive insights into the stock market.
        </p>
      </div>

      {/* Key Features Section */}
      <div className="bg-gradient-to-r from-green-50 to-yellow-50 p-6 rounded-lg shadow-md mb-8">
        <h2 className="text-2xl font-bold text-center mb-4 text-gray-800">Key Features</h2>
        <ul className="list-disc pl-8 text-lg text-gray-700">
          <li className="mb-2 bg-white p-3 rounded-lg shadow-sm">View stock charts for real-time market data.</li>
          <li className="mb-2 bg-white p-3 rounded-lg shadow-sm">Access detailed stock tables for in-depth analysis.</li>
          <li className="mb-2 bg-white p-3 rounded-lg shadow-sm">Stay updated with the latest news and market trends.</li>
        </ul>
      </div>
    </div>
  );
}

export default About;