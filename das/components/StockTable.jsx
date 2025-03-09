import {useEffect, useState} from "react";

function StockTable({code}) {
    // {"final_decision": "Buy", "news_signal": "Buy", "last_report_signal": "Hold", "prediction_signal": "Buy"}
    const [signals, setSignals] = useState({})

    useEffect(() => {
        // fetch(`http://localhost:8000/api/predictions/?code=${code}`)
        //     .then((response) => response.json())
        //     .then((data) => setSignals(data))
        //     .catch((error) => console.error("Error fetching codes:", error));
    }, [code]);

    return (
        <div className="p-4 bg-white shadow rounded-md">
            <h2 className="text-lg font-bold mb-4">Stock Details</h2>
            <table className="w-full text-left border-collapse">
                <thead>
                <tr>
                    <th className="border-b p-2">Last Report Signal</th>
                    <th className="border-b p-2">News Signal</th>
                    <th className="border-b p-2">Prediction Signal</th>
                    <th className="border-b p-2 font-bold">Final Decision</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td className={`border-b border-black p-2 ${signals["last_report_signal"] === "Buy" ? "text-green-500" : signals["last_report_signal"] === "Sell" ? "text-red-500" : "text-yellow-500"}`}>
                        {signals["last_report_signal"]}
                    </td>
                    <td className={`border-b border-black p-2 ${signals["news_signal"] === "Buy" ? "text-green-500" : signals["news_signal"] === "Sell" ? "text-red-500" : "text-yellow-500"}`}>
                        {signals["news_signal"]}
                    </td>
                    <td className={`border-b border-black p-2 ${signals["prediction_signal"] === "Buy" ? "text-green-500" : signals["prediction_signal"] === "Sell" ? "text-red-500" : "text-yellow-500"}`}>
                        {signals["prediction_signal"]}
                    </td>
                    <td className={`border-b border-black p-2 font-bold ${signals["final_decision"] === "Buy" ? "text-green-500" : signals["final_decision"] === "Sell" ? "text-red-500" : "text-yellow-500"}`}>
                        {signals["final_decision"]}
                    </td>
                </tr>


                </tbody>
            </table>
        </div>
    );
}

export default StockTable