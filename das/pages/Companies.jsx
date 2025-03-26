import {useEffect, useState} from "react";
import CodeDropdown from "../components/CodeDropdown.jsx";
import StockChart from "../components/StockChart.jsx";
import StockTable from "../components/StockTable.jsx";
import NewsComponent from "../components/NewsTable.jsx";

function Companies() {
    const [code, setCode] = useState(localStorage.getItem('selectedStockCode') || "ABT");
    const [updated, setUpdated] = useState(false)
    const [isLoading, setIsLoading] = useState(false);
    const [dataVersion, setDataVersion] = useState(0);

    useEffect(() => {
      const updateAndRefresh = async () => {
        try {
          // 1. Wait for scraping to complete
          await fetch(`http://localhost:8000/update/table/?code=${code}`);

          // 2. Force fresh data fetch after update
          setUpdated(prev => !prev);

          // 3. Add small delay to ensure backend persistence
          await new Promise(resolve => setTimeout(resolve, 500));

        } catch (error) {
          console.error("Update failed:", error);
        }
      };

      updateAndRefresh();
    }, [code]); // Trigger on code change


    return (
        <div>
            <CodeDropdown setCode={setCode}/>
            {isLoading && <div>Updating data for {code}...</div>}
            {/*<button onClick={handleUpdate}>Update</button>*/}
            <div className="grid grid-cols-4 grid-rows-2 gap-6 mt-6">
                {/* First row: StockChart takes 3/4, NewsComponent takes 1/4 */}
                <div className="col-span-3 row-span-1 bg-white p-4 rounded-md shadow">
                    <StockChart code={code} updated={updated} dataVersion={dataVersion}/>
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
