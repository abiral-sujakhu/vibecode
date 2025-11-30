import { Constituency } from '../data/constituencies';

interface ConstituencyCardProps {
  constituency: Constituency;
}

export default function ConstituencyCard({ constituency }: ConstituencyCardProps) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-xl transition-shadow duration-300">
      {/* Constituency Name */}
      <h2 className="text-2xl font-bold text-gray-800 mb-4 border-b-2 border-blue-500 pb-2">
        {constituency.name}
      </h2>

      {/* Rankings */}
      <div className="space-y-3">
        {constituency.topThree.map((politician, index) => (
          <div 
            key={index}
            className="flex items-start gap-3 p-3 bg-gray-50 rounded-md hover:bg-gray-100 transition-colors"
          >
            {/* Rank Badge */}
            <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center font-bold text-white ${
              index === 0 ? 'bg-yellow-500' : 
              index === 1 ? 'bg-gray-400' : 
              'bg-amber-700'
            }`}>
              {index + 1}
            </div>

            {/* Politician Details */}
            <div className="flex-1 min-w-0">
              <h3 className="text-lg font-semibold text-gray-800 truncate">
                {politician.name}
              </h3>
              <div className="flex items-center justify-between mt-1">
                <p className="text-sm text-blue-600 font-medium truncate">
                  {politician.party}
                </p>
                <p className="text-sm text-gray-600 font-semibold ml-2">
                  {politician.votes.toLocaleString()} votes
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
