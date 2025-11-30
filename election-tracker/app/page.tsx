import ConstituencyCard from './components/ConstituencyCard';
import { constituenciesData } from './data/constituencies';

export default function Home() {
  return (
    <div className="min-h-screen bg-linear-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <header className="bg-white shadow-md">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-800 text-center">
            Election Tracker 2025
          </h1>
          <p className="text-center text-gray-600 mt-2">
            Kathmandu Constituency Results
          </p>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        {/* Grid Layout for Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {constituenciesData.map((constituency, index) => (
            <ConstituencyCard key={index} constituency={constituency} />
          ))}
        </div>
      </main>
    </div>
  );
}
