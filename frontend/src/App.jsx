import axios from 'axios';
import React, { useState } from 'react';
import { Loader2 } from 'lucide-react'; // Optional: Install lucide-react for icons

const App = () => {
  const [email, setEmail] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const validateMail = async () => {
    try {
      setLoading(true);
      setResult(null);
      const response = await axios.post('https://spam-mail-detector-1.onrender.com/predict', { email });
      setResult(response.data);
    } catch (error) {
      console.error('Validation failed:', error);
      setResult({ error: 'Validation failed. Please try again.' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-100 to-blue-200 p-4">
      <div className="bg-white shadow-2xl rounded-3xl p-10 max-w-5xl w-full space-y-4 transition-all duration-300">
        <h1 className="text-3xl font-bold text-center text-indigo-700 tracking-wide">
          🛡️ Spam Mail Detector
        </h1>

        <textarea
          rows={15}
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="📧 Paste the full email content here..."
          className="w-full px-5 py-4 border-2 border-indigo-300 rounded-xl text-gray-800 text-base resize-none focus:outline-none focus:ring-2 focus:ring-indigo-300 shadow-inner"
        />

        <button
          onClick={validateMail}
          disabled={loading || email.trim() === ''}
          className="w-full flex items-center justify-center gap-2 bg-indigo-600 hover:bg-indigo-700 disabled:bg-indigo-300 text-white font-semibold text-lg py-2 rounded-xl transition-all duration-200 shadow-md"
        >
          {loading && <Loader2 className="animate-spin w-5 h-5" />}
          {loading ? 'Validating...' : 'Validate Email'}
        </button>

        {result && (
          <div
            className={`mt-6 px-6 py-4 rounded-xl text-center text-lg font-medium transition-all duration-300 ${
              result.error
                ? 'bg-red-100 text-red-700'
                : result.isSpam
                ? 'bg-red-50 text-red-600 border border-red-300'
                : 'bg-green-50 text-green-600 border border-green-300'
            }`}
          >
            {result.error
              ? result.error
              : result.isSpam
              ? '🚨 This appears to be a Spam Email!'
              : '✅ This email is clean and not spam.'}
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
