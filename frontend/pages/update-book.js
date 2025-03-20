// pages/update-book.js
import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import { updateBook, fetchBooks } from "../utils/api";
import { toast } from "react-toastify";
import Link from "next/link";

export default function UpdateBook() {
  const router = useRouter();
  const { id } = router.query;

  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [borrower, setBorrower] = useState("");

  useEffect(() => {
    if (id) {
      const token = localStorage.getItem("token");
      fetchBooks(token)
        .then((books) => {
          const book = books.find((b) => b.id == id);
          if (book) {
            setTitle(book.title);
            setAuthor(book.author);
            setBorrower(book.borrower || "");
          }
        })
        .catch((err) => console.error(err));
    }
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem("token");
    try {
      const response = await updateBook(token, id, { title, author, borrower });
      toast.success(response.message);
      router.push("/dashboard");
    } catch (error) {
      toast.error(error.error || "Failed to update book");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h2 className="text-2xl font-bold mb-4">Update Book</h2>
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
          Update Book
        </button>
        <Link href="/dashboard" className="mt-4 text-center block text-blue-600">
          Cancel
        </Link>
      </form>
    </div>
  );
}
