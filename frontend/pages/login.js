import { useState } from "react";
import { loginUser } from "../utils/api";
import { useRouter } from "next/router";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const router = useRouter();

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const data = await loginUser(username, password);
            localStorage.setItem("token", data.token);
            toast.success("Login successful!");
            router.push("/dashboard");
        } catch (error) {
            toast.error(error.error || "Login failed");
        }
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
            <h2 className="text-2xl font-bold mb-4">Login</h2>
            <form onSubmit={handleLogin} className="bg-white p-6 shadow-md rounded">
                <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} className="block w-full p-2 border rounded mb-2" required />
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} className="block w-full p-2 border rounded mb-2" required />
                <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">Login</button>
            </form>
        </div>
    );
}
