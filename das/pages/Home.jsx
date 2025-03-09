import React from "react";

function Home() {
  return (
    <div className="bg-white p-6 rounded-md shadow-md">
      <h2 className="text-2xl font-bold mb-4">About Stocks</h2>
      <p className="text-gray-700">
        Stocks are financial instruments that represent ownership in a company. When you buy a stock, you're
        purchasing a small part of that company. Stocks are traded on stock exchanges and can fluctuate in value
        based on a variety of factors, including the company's financial health, market conditions, and economic
        news.
      </p>

      <h3 className="text-xl font-semibold mt-6 mb-2">Types of Stocks</h3>
      <ul className="list-disc pl-6 text-gray-700">
        <li><strong>Common Stocks:</strong> Represents ownership in a company and a claim on part of the profits.</li>
        <li><strong>Preferred Stocks:</strong> Gives investors a priority claim on dividends but usually does not carry voting rights.</li>
      </ul>

      <h3 className="text-xl font-semibold mt-6 mb-2">Stock Market Basics</h3>
      <p className="text-gray-700">
        The stock market is where buyers and sellers come together to trade stocks. It's an essential part of the
        global economy, providing companies with access to capital and investors with opportunities for growth.
        Stock prices are determined by supply and demand dynamics, meaning that if more people want to buy a stock
        than sell it, the price goes up.
      </p>

      <h3 className="text-xl font-semibold mt-6 mb-2">Why Invest in Stocks?</h3>
      <p className="text-gray-700">
        Investing in stocks can be a way to build wealth over time, as stocks tend to grow in value over the long term.
        However, investing in stocks involves risks, and prices can fluctuate in the short term. It's important to do
        thorough research before making investment decisions.
      </p>
    </div>
  );
}

export default Home;
