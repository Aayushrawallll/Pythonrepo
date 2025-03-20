import Link from 'next/link';
import { useRouter } from 'next/router';

const Navbar = () => {
  const router = useRouter();
  const token = typeof window !== 'undefined' ? localStorage.getItem('token') : null;

  const handleLogout = () => {
    localStorage.removeItem('token');
    router.push('/login');
  };

  return (
    <nav className="bg-white shadow-md p-4 flex justify-between items-center">
      <div className="text-2xl font-bold">Book Management</div>
      <div className="space-x-4">
        {!token ? (
          <>
            <Link href="/login" legacyBehavior>
              <a className="text-blue-500 hover:underline">Login</a>
            </Link>
            <Link href="/register" legacyBehavior>
              <a className="text-blue-500 hover:underline">Register</a>
            </Link>
          </>
        ) : (
          <button onClick={handleLogout} className="bg-red-500 text-white px-4 py-2 rounded">
            Logout
          </button>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
