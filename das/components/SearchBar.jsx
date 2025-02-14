function SearchBar() {
  return (
    <div className="flex items-center space-x-4">
      <input
        type="text"
        placeholder="Search stock symbol..."
        className="w-full p-2 border rounded-md"
      />
      <button className="bg-blue-600 text-white px-4 py-2 rounded-md">
        Search
      </button>
    </div>
  );
}

export default SearchBar