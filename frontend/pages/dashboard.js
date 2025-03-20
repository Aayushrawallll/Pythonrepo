import { useEffect, useState } from 'react';
import { fetchBooks, deleteBook } from '../utils/api';
import { useRouter } from 'next/router';
import Link from 'next/link';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import LogoutButton from '../components/LogoutButton';

export default function Dashboard() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      router.push('/login');
      return;
    }

    fetchBooks(token)
      .then((data) => {
        setBooks(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setLoading(false);
      });
  }, [router]);

  const handleDelete = async (id) => {
    const isConfirmed = window.confirm('Are you sure you want to delete this book?');
    if (!isConfirmed) return;

    const token = localStorage.getItem('token');
    try {
      await deleteBook(token, id);
      setBooks(books.filter((book) => book.id !== id));
      toast.success('Book deleted successfully!');
    } catch (error) {
      toast.error('Failed to delete book.');
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="p-6">
      <ToastContainer />
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Books List</h1>
        <LogoutButton />
      </div>
      <div className="mb-4">
        <Link href="/add-book" legacyBehavior>
          <a className="bg-blue-500 text-white px-4 py-2 rounded">Add New Book</a>
        </Link>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {books.map((book) => (
          <div key={book.id} className="border rounded-lg p-4 bg-white shadow-md">
            <h2 className="text-xl font-semibold mb-2">{book.title}</h2>
            <p className="text-gray-700 mb-1">Author: {book.author}</p>
            <p className="text-gray-700 mb-3">Borrower: {book.borrower || 'N/A'}</p>
            <div className="flex justify-between">
              <Link href={`/update-book?id=${book.id}`} legacyBehavior>
                <a className="bg-green-500 text-white px-3 py-1 rounded">Edit</a>
              </Link>
              <button
                className="bg-red-500 text-white px-3 py-1 rounded"
                onClick={() => handleDelete(book.id)}
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
