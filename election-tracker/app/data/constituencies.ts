export interface Politician {
  name: string;
  votes: number;
  party: string;
}

export interface Constituency {
  name: string;
  topThree: Politician[];
}

export const constituenciesData: Constituency[] = [
  {
    name: "Kathmandu-1",
    topThree: [
      { name: "Rajesh Kumar Sharma", votes: 45230, party: "Nepal Congress" },
      { name: "Sita Devi Thapa", votes: 42150, party: "CPN-UML" },
      { name: "Prakash Bahadur Rai", votes: 38900, party: "Maoist Centre" }
    ]
  },
  {
    name: "Kathmandu-2",
    topThree: [
      { name: "Amrita Kumari Shrestha", votes: 48600, party: "CPN-UML" },
      { name: "Dipak Prasad Joshi", votes: 44320, party: "Nepal Congress" },
      { name: "Binita Sharma", votes: 39870, party: "Rastriya Swatantra Party" }
    ]
  },
  {
    name: "Kathmandu-3",
    topThree: [
      { name: "Narayan Singh Tamang", votes: 52100, party: "Maoist Centre" },
      { name: "Gita Devi Karki", votes: 47890, party: "Nepal Congress" },
      { name: "Ravi Kumar Adhikari", votes: 41200, party: "CPN-UML" }
    ]
  },
  {
    name: "Kathmandu-4",
    topThree: [
      { name: "Krishna Bahadur Mahara", votes: 49800, party: "Rastriya Swatantra Party" },
      { name: "Sunita Rani Thakur", votes: 46500, party: "Nepal Congress" },
      { name: "Bhim Prasad Gautam", votes: 43100, party: "CPN-UML" }
    ]
  },
  {
    name: "Kathmandu-5",
    topThree: [
      { name: "Anita Kumari Basnet", votes: 51200, party: "Nepal Congress" },
      { name: "Mohan Lal Shrestha", votes: 48900, party: "CPN-UML" },
      { name: "Ramesh Kumar Yadav", votes: 44600, party: "Rastriya Prajatantra Party" }
    ]
  },
  {
    name: "Kathmandu-6",
    topThree: [
      { name: "Bijay Kumar Gajurel", votes: 47300, party: "CPN-UML" },
      { name: "Pramila Sharma Poudel", votes: 45100, party: "Nepal Congress" },
      { name: "Suresh Bahadur Ale", votes: 42800, party: "Maoist Centre" }
    ]
  },
  {
    name: "Kathmandu-7",
    topThree: [
      { name: "Kalpana Devi Pandey", votes: 53400, party: "Rastriya Swatantra Party" },
      { name: "Hari Prasad Dahal", votes: 49200, party: "Nepal Congress" },
      { name: "Laxmi Kumari Shakya", votes: 46700, party: "CPN-UML" }
    ]
  },
  {
    name: "Kathmandu-8",
    topThree: [
      { name: "Deepak Kumar Manandhar", votes: 50600, party: "Nepal Congress" },
      { name: "Radha Krishna Maharjan", votes: 48300, party: "CPN-UML" },
      { name: "Sarita Devi Gurung", votes: 44900, party: "Rastriya Swatantra Party" }
    ]
  },
  {
    name: "Kathmandu-9",
    topThree: [
      { name: "Pratima Kumari Rana", votes: 49900, party: "CPN-UML" },
      { name: "Anil Kumar Thapa", votes: 47600, party: "Maoist Centre" },
      { name: "Shanti Devi Limbu", votes: 43200, party: "Nepal Congress" }
    ]
  },
  {
    name: "Kathmandu-10",
    topThree: [
      { name: "Gopal Prasad Rizal", votes: 52800, party: "Nepal Congress" },
      { name: "Maya Kumari Tamang", votes: 48700, party: "Rastriya Swatantra Party" },
      { name: "Bharat Singh Tharu", votes: 45300, party: "CPN-UML" }
    ]
  }
];
