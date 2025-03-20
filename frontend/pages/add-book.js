// pages/add-book.js
import { useState } from "react";
import { addBook } from "../utils/api";
import { useRouter } from "next/router";
import { toast } from "react-toastify";

export default function AddBook() {
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [borrower, setBorrower] = useState("");
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem("token");
    try {
      const response = await addBook(token, { title, author, borrower });
      toast.success(response.message);
      router.push("/dashboard");
    } catch (error) {
      toast.error(error.error || "Failed to add book");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h2 className="text-2xl font-bold mb-4">Add a New Book</h2>
      <form onSubmit={handleSubmit} className="bg-white p-6 shadow-md rounded w-96">
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="block w-full p-2 border rounded mb-2"
          required
        />
        <input
          type="text"
          placeholder="Author"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
          className="block w-full p-2 border rounded mb-2"
          required
        />
        <input
          type="text"
          placeholder="Borrower"
          value={borrower}
          onChange={(e) => setBorrower(e.target.value)}
          className="block w-full p-2 border rounded mb-2"
        />
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded w-full">
          Add Book
        </button>
      </form>
    </div>
  );
}
