import {useEffect, useState} from "react";
import CodeDropdown from "../components/CodeDropdown.jsx";
import StockChart from "../components/StockChart.jsx";
import StockTable from "../components/StockTable.jsx";
import NewsComponent from "../components/NewsTable.jsx";

function Companies() {
    const [code, setCode] = useState("ABT");
    const [updated, setUpdated] = useState(false)

    useEffect(() => {
        console.log("updating")
        fetch(`http://localhost:8000/update/table/?code=${code}`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then((data) => {
                console.log("Update successful:", data);
                setUpdated(true)
            })
            .catch((error) => {
                console.error("Error updating:", error);
            });
    }, [code]);

    return (
        <div>
            <CodeDropdown setCode={setCode}/>
            {/*<button onClick={handleUpdate}>Update</button>*/}
            <div className="grid grid-cols-4 grid-rows-2 gap-6 mt-6">
                {/* First row: StockChart takes 3/4, NewsComponent takes 1/4 */}
                <div className="col-span-3 row-span-1 bg-white p-4 rounded-md shadow">
                    <StockChart code={code} updated={updated}/>
                </div>
                <div className="col-span-1 row-span-1 bg-white p-4 rounded-md shadow">
                    <NewsComponent code={code} updated={updated}/>
                </div>

                {/* Second row: StockTable spans full width */}
                <div className="col-span-4 row-span-1 bg-white p-4 rounded-md shadow">
                    <StockTable code={code} updated={updated}/>
                </div>
            </div>
        </div>
    );
}

export default Companies;
