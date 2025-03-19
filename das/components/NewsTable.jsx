import { useEffect, useState } from "react";

function NewsComponent({ code, updated }) {
    const [news, setNews] = useState([]);
    const [expandedArticleId, setExpandedArticleId] = useState(null);

    useEffect(() => {
        fetch(`http://localhost:8000/api/db-news/?code=${code}`)
            .then((response) => response.json())
            .then((data) => {
                // Assuming the API returns an array of news objects
                if (Array.isArray(data)) {
                    setNews(data);
                } else {
                    console.error("Invalid data format:", data);
                }
            })
            .catch((error) => console.error("Error fetching news:", error));
    }, [code, updated]);

    const handleTitleClick = (id) => {
        setExpandedArticleId(expandedArticleId === id ? null : id);
    };

    return (
        <div className="bg-white p-4 rounded-md shadow h-[57vh] overflow-y-scroll">
            <h2 className="text-lg font-bold mb-2">Latest News</h2>
            <ul>
                {news.length > 0 ? (
                    news.map((article) => (
                        <li key={article.id} className="mb-3 border-b pb-2">
                            <h3
                                className="font-semibold cursor-pointer hover:text-blue-600"
                                onClick={() => handleTitleClick(article.id)}
                            >
                                ● {article.title}
                            </h3>
                            {expandedArticleId === article.id && (
                                <p className="text-gray-600 mt-2">{article.summary}</p>
                            )}
                        </li>
                    ))
                ) : (
                    <p className="text-gray-500">No news available.</p>
                )}
            </ul>
        </div>
    );
}

export default NewsComponent;