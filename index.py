import React, { useState } from 'react';
import { Bot, Heart, Star, Target, BookOpen, Trophy, ChevronRight, User, MessageCircle, Map, Sparkles, Brain, Calculator, Palette, Music, Microscope, Globe, Wrench, Users } from 'lucide-react';

const AICareerCounselor = () => {
  const [currentStep, setCurrentStep] = useState('interests');
  const [userInput, setUserInput] = useState('');
  const [conversation, setConversation] = useState([]);
  const [selectedInterests, setSelectedInterests] = useState([]);
  const [userProfile, setUserProfile] = useState({
    name: '',
    age: '',
    education: '',
    experience: ''
  });
  const [generatedRoadmap, setGeneratedRoadmap] = useState(null);

  const interestCategories = [
    { id: 'math', name: 'Mathematics', icon: Calculator, description: 'Numbers, equations, problem-solving' },
    { id: 'science', name: 'Science', icon: Microscope, description: 'Biology, chemistry, physics, research' },
    { id: 'technology', name: 'Technology', icon: Bot, description: 'Computers, programming, AI, gadgets' },
    { id: 'arts', name: 'Arts & Design', icon: Palette, description: 'Visual arts, creativity, aesthetics' },
    { id: 'music', name: 'Music & Audio', icon: Music, description: 'Sound, composition, performance' },
    { id: 'language', name: 'Languages', icon: Globe, description: 'Communication, writing, linguistics' },
    { id: 'business', name: 'Business', icon: Target, description: 'Finance, management, entrepreneurship' },
    { id: 'social', name: 'Social Work', icon: Users, description: 'Helping people, community service' },
    { id: 'health', name: 'Health & Medicine', icon: Heart, description: 'Healthcare, wellness, biology' },
    { id: 'engineering', name: 'Engineering', icon: Wrench, description: 'Building, mechanics, problem-solving' },
    { id: 'psychology', name: 'Psychology', icon: Brain, description: 'Human behavior, mental health' },
    { id: 'education', name: 'Education', icon: BookOpen, description: 'Teaching, learning, knowledge sharing' }
  ];

  const careerDatabase = {
    'math,technology': {
      careers: ['Data Scientist', 'Software Engineer', 'Machine Learning Engineer', 'Quantitative Analyst', 'Cybersecurity Specialist'],
      example: 'Data Scientist'
    },
    'science,health': {
      careers: ['Medical Doctor', 'Biomedical Engineer', 'Pharmacist', 'Research Scientist', 'Nurse Practitioner'],
      example: 'Medical Doctor'
    },
    'arts,technology': {
      careers: ['UX/UI Designer', 'Game Designer', 'Digital Artist', 'Web Designer', 'Animation Artist'],
      example: 'UX/UI Designer'
    },
    'business,technology': {
      careers: ['Product Manager', 'Business Analyst', 'Tech Entrepreneur', 'Digital Marketing Manager', 'Sales Engineer'],
      example: 'Product Manager'
    },
    'music,technology': {
      careers: ['Sound Engineer', 'Music Producer', 'Audio Software Developer', 'Podcast Producer', 'Music Therapist'],
      example: 'Sound Engineer'
    },
    'language,technology': {
      careers: ['Technical Writer', 'Translator', 'Content Creator', 'SEO Specialist', 'Communications Manager'],
      example: 'Technical Writer'
    },
    'social,psychology': {
      careers: ['Social Worker', 'Counselor', 'Human Resources Manager', 'Community Organizer', 'Therapist'],
      example: 'Counselor'
    },
    'engineering,technology': {
      careers: ['Software Engineer', 'Robotics Engineer', 'Systems Administrator', 'DevOps Engineer', 'Hardware Engineer'],
      example: 'Robotics Engineer'
    },
    'education,technology': {
      careers: ['Instructional Designer', 'Educational Technology Specialist', 'Online Course Creator', 'Learning Analyst', 'EdTech Entrepreneur'],
      example: 'Instructional Designer'
    }
  };

  const generatePersonalizedRoadmap = (interests) => {
    const interestKey = interests.slice(0, 2).join(',');
    const careerInfo = careerDatabase[interestKey] || careerDatabase['technology,math'];
    
    const roadmapTemplates = {
      'Data Scientist': {
        title: 'Data Scientist',
        description: 'Analyze complex data to help businesses make informed decisions',
        timeline: '8-12 months',
        roadmap: [
          { 
            title: 'Foundation: Math & Statistics', 
            duration: '2-3 months', 
            skills: ['Statistics', 'Linear Algebra', 'Probability', 'Calculus basics'],
            resources: ['Khan Academy Math', 'Coursera Statistics', 'YouTube 3Blue1Brown']
          },
          { 
            title: 'Programming Skills', 
            duration: '2-3 months', 
            skills: ['Python', 'SQL', 'Pandas', 'NumPy'],
            resources: ['Python.org tutorial', 'W3Schools SQL', 'Kaggle Learn']
          },
          { 
            title: 'Data Analysis & Visualization', 
            duration: '2-3 months', 
            skills: ['Matplotlib', 'Seaborn', 'Tableau', 'Power BI'],
            resources: ['Tableau Public', 'Seaborn documentation', 'Data visualization courses']
          },
          { 
            title: 'Machine Learning', 
            duration: '3-4 months', 
            skills: ['Scikit-learn', 'TensorFlow', 'Model evaluation', 'Deep learning'],
            resources: ['Andrew Ng ML Course', 'Fast.ai', 'Google ML Crash Course']
          }
        ],
        salary: '$70,000 - $150,000',
        growth: 'Very high demand, 35% job growth expected',
        nextSteps: ['Build portfolio projects', 'Contribute to open source', 'Network with data professionals']
      },
      'Medical Doctor': {
        title: 'Medical Doctor',
        description: 'Diagnose and treat patients, save lives and improve health',
        timeline: '8-12 years',
        roadmap: [
          { 
            title: 'Pre-Medical Education', 
            duration: '4 years', 
            skills: ['Biology', 'Chemistry', 'Physics', 'MCAT preparation'],
            resources: ['University pre-med programs', 'MCAT prep courses', 'Medical volunteering']
          },
          { 
            title: 'Medical School', 
            duration: '4 years', 
            skills: ['Anatomy', 'Physiology', 'Pathology', 'Clinical skills'],
            resources: ['Medical school curriculum', 'USMLE Step 1 & 2', 'Clinical rotations']
          },
          { 
            title: 'Residency Training', 
            duration: '3-7 years', 
            skills: ['Specialized medical knowledge', 'Patient care', 'Medical procedures'],
            resources: ['Residency programs', 'Medical conferences', 'Peer learning']
          },
          { 
            title: 'Board Certification', 
            duration: '1 year', 
            skills: ['Specialty expertise', 'Board exams', 'Continuing education'],
            resources: ['Board certification exams', 'Medical associations', 'CME courses']
          }
        ],
        salary: '$200,000 - $400,000+',
        growth: 'Stable demand, essential profession',
        nextSteps: ['Choose specialization', 'Build patient relationships', 'Stay updated with medical advances']
      },
      'UX/UI Designer': {
        title: 'UX/UI Designer',
        description: 'Create beautiful and user-friendly digital experiences',
        timeline: '6-10 months',
        roadmap: [
          { 
            title: 'Design Fundamentals', 
            duration: '2-3 months', 
            skills: ['Color theory', 'Typography', 'Layout principles', 'Visual hierarchy'],
            resources: ['Design principles courses', 'Adobe tutorials', 'Dribbble inspiration']
          },
          { 
            title: 'UX Research & Strategy', 
            duration: '2-3 months', 
            skills: ['User research', 'Personas', 'User journey mapping', 'Wireframing'],
            resources: ['UX research methods', 'Figma tutorials', 'UX case studies']
          },
          { 
            title: 'Design Tools Mastery', 
            duration: '2-3 months', 
            skills: ['Figma', 'Adobe XD', 'Sketch', 'Prototyping'],
            resources: ['Figma Academy', 'Adobe XD tutorials', 'Design tool documentation']
          },
          { 
            title: 'Portfolio & Job Prep', 
            duration: '2-3 months', 
            skills: ['Portfolio creation', 'Case studies', 'Interview skills', 'Design critique'],
            resources: ['Portfolio examples', 'UX interview prep', 'Design communities']
          }
        ],
        salary: '$60,000 - $120,000',
        growth: 'High demand, digital transformation driving growth',
        nextSteps: ['Build strong portfolio', 'Network with designers', 'Keep up with design trends']
      }
    };

    const selectedCareer = careerInfo.example;
    return roadmapTemplates[selectedCareer] || roadmapTemplates['Data Scientist'];
  };

  const handleInterestToggle = (interestId) => {
    setSelectedInterests(prev => 
      prev.includes(interestId) 
        ? prev.filter(id => id !== interestId)
        : [...prev, interestId]
    );
  };

  const generateRoadmap = () => {
    if (selectedInterests.length === 0) {
      alert('Please select at least one interest!');
      return;
    }
    
    const roadmap = generatePersonalizedRoadmap(selectedInterests);
    setGeneratedRoadmap(roadmap);
    setCurrentStep('roadmap');
  };

  const handleChat = () => {
    if (!userInput.trim()) return;
    
    const response = `Great question! Based on your interests in ${selectedInterests.join(', ')}, I can see you're passionate about diverse fields. This combination opens up many exciting career possibilities! Your personalized roadmap will help you leverage these interests. Feel free to ask me anything about your career journey! 🌟`;
    
    setConversation([
      ...conversation,
      { type: 'user', message: userInput },
      { type: 'ai', message: response }
    ]);
    setUserInput('');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-100 via-pink-50 to-blue-100 p-4">
      {/* Header */}
      <div className="max-w-6xl mx-auto mb-6">
        <div className="bg-white rounded-3xl shadow-lg p-6 border-2 border-purple-200">
          <div className="flex items-center justify-center gap-3 mb-4">
            <div className="bg-gradient-to-r from-purple-500 to-pink-500 p-3 rounded-full">
              <Bot className="w-8 h-8 text-white" />
            </div>
            <h1 className="text-3xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
              AI Career Counselor
            </h1>
            <Heart className="w-6 h-6 text-pink-500" />
          </div>
          <p className="text-center text-gray-600 text-lg">
            Discover your perfect career path based on your unique interests! ✨
          </p>
        </div>
      </div>

      {/* Navigation */}
      <div className="max-w-6xl mx-auto mb-6">
        <div className="flex gap-2 justify-center flex-wrap">
          <button
            onClick={() => setCurrentStep('interests')}
            className={`px-6 py-3 rounded-full font-semibold transition-all ${
              currentStep === 'interests' 
                ? 'bg-purple-500 text-white shadow-lg' 
                : 'bg-white text-purple-600 hover:bg-purple-50'
            }`}
          >
            <Star className="w-4 h-4 inline mr-2" />
            Choose Interests
          </button>
          <button
            onClick={() => setCurrentStep('chat')}
            className={`px-6 py-3 rounded-full font-semibold transition-all ${
              currentStep === 'chat' 
                ? 'bg-purple-500 text-white shadow-lg' 
                : 'bg-white text-purple-600 hover:bg-purple-50'
            }`}
          >
            <MessageCircle className="w-4 h-4 inline mr-2" />
            Chat
          </button>
          <button
            onClick={() => setCurrentStep('roadmap')}
            className={`px-6 py-3 rounded-full font-semibold transition-all ${
              currentStep === 'roadmap' 
                ? 'bg-purple-500 text-white shadow-lg' 
                : 'bg-white text-purple-600 hover:bg-purple-50'
            }`}
          >
            <Map className="w-4 h-4 inline mr-2" />
            Your Roadmap
          </button>
        </div>
      </div>

      {/* Interest Selection */}
      {currentStep === 'interests' && (
        <div className="max-w-6xl mx-auto">
          <div className="bg-white rounded-3xl shadow-lg p-6 border-2 border-purple-200">
            <div className="text-center mb-8">
              <Sparkles className="w-12 h-12 text-purple-500 mx-auto mb-4" />
              <h2 className="text-3xl font-bold text-purple-600 mb-2">What Are You Passionate About?</h2>
              <p className="text-gray-600 text-lg">Select all the fields that interest you. Don't worry, you can choose multiple!</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 mb-8">
              {interestCategories.map((category) => {
                const Icon = category.icon;
                const isSelected = selectedInterests.includes(category.id);
                
                return (
                  <button
                    key={category.id}
                    onClick={() => handleInterestToggle(category.id)}
                    className={`p-4 rounded-2xl border-2 transition-all hover:shadow-lg ${
                      isSelected 
                        ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white border-purple-500' 
                        : 'bg-white border-purple-200 hover:border-purple-400'
                    }`}
                  >
                    <Icon className={`w-8 h-8 mx-auto mb-2 ${isSelected ? 'text-white' : 'text-purple-500'}`} />
                    <h3 className={`font-semibold mb-1 ${isSelected ? 'text-white' : 'text-purple-700'}`}>
                      {category.name}
                    </h3>
                    <p className={`text-sm ${isSelected ? 'text-purple-100' : 'text-gray-600'}`}>
                      {category.description}
                    </p>
                  </button>
                );
              })}
            </div>

            {selectedInterests.length > 0 && (
              <div className="text-center">
                <div className="bg-purple-50 p-4 rounded-2xl mb-6 border-2 border-purple-200">
                  <h3 className="font-semibold text-purple-700 mb-2">Your Selected Interests:</h3>
                  <div className="flex flex-wrap gap-2 justify-center">
                    {selectedInterests.map(interestId => {
                      const interest = interestCategories.find(cat => cat.id === interestId);
                      return (
                        <span key={interestId} className="bg-purple-500 text-white px-3 py-1 rounded-full text-sm">
                          {interest?.name}
                        </span>
                      );
                    })}
                  </div>
                </div>
                
                <button
                  onClick={generateRoadmap}
                  className="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-8 py-4 rounded-2xl font-semibold hover:shadow-lg transition-all text-lg"
                >
                  Generate My Career Roadmap! 🚀
                </button>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Chat Interface */}
      {currentStep === 'chat' && (
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-3xl shadow-lg p-6 border-2 border-purple-200">
            <div className="h-96 overflow-y-auto mb-4 p-4 bg-gray-50 rounded-2xl">
              {conversation.length === 0 && (
                <div className="text-center py-8">
                  <MessageCircle className="w-12 h-12 text-purple-400 mx-auto mb-4" />
                  <p className="text-gray-500 text-lg">
                    {selectedInterests.length > 0 
                      ? `Great! I see you're interested in ${selectedInterests.join(', ')}. Ask me anything about your career journey!`
                      : 'First, go to "Choose Interests" to select what you\'re passionate about!'
                    }
                  </p>
                </div>
              )}
              
              {conversation.map((msg, index) => (
                <div key={index} className={`mb-4 ${msg.type === 'user' ? 'text-right' : 'text-left'}`}>
                  <div className={`inline-block p-3 rounded-2xl max-w-xs ${
                    msg.type === 'user' 
                      ? 'bg-purple-500 text-white' 
                      : 'bg-white border-2 border-purple-200'
                  }`}>
                    {msg.message}
                  </div>
                </div>
              ))}
            </div>

            <div className="flex gap-3">
              <input
                type="text"
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleChat()}
                placeholder="Ask me about careers, skills, or your future..."
                className="flex-1 p-4 border-2 border-purple-200 rounded-2xl focus:outline-none focus:border-purple-500"
              />
              <button
                onClick={handleChat}
                className="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-6 py-4 rounded-2xl hover:shadow-lg transition-all"
              >
                Send
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Roadmap View */}
      {currentStep === 'roadmap' && (
        <div className="max-w-6xl mx-auto">
          {generatedRoadmap ? (
            <div className="bg-white rounded-3xl shadow-lg p-6 border-2 border-purple-200">
              <div className="text-center mb-8">
                <Trophy className="w-12 h-12 text-yellow-500 mx-auto mb-4" />
                <h2 className="text-3xl font-bold text-purple-600 mb-2">{generatedRoadmap.title}</h2>
                <p className="text-gray-600 text-lg mb-4">{generatedRoadmap.description}</p>
                <div className="bg-blue-50 p-3 rounded-2xl inline-block">
                  <span className="text-blue-700 font-semibold">⏱️ Timeline: {generatedRoadmap.timeline}</span>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <div className="bg-green-50 p-4 rounded-2xl border-2 border-green-200">
                  <h3 className="font-semibold text-green-800 mb-2">💰 Salary Range</h3>
                  <p className="text-green-700">{generatedRoadmap.salary}</p>
                </div>
                <div className="bg-blue-50 p-4 rounded-2xl border-2 border-blue-200">
                  <h3 className="font-semibold text-blue-800 mb-2">📈 Growth Outlook</h3>
                  <p className="text-blue-700">{generatedRoadmap.growth}</p>
                </div>
              </div>

              <h3 className="text-2xl font-bold text-purple-600 mb-6 text-center">
                Your Personalized Learning Journey 🗺️
              </h3>

              <div className="space-y-6 mb-8">
                {generatedRoadmap.roadmap.map((step, index) => (
                  <div key={index} className="flex items-start gap-4">
                    <div className="bg-purple-500 text-white w-10 h-10 rounded-full flex items-center justify-center font-bold text-lg">
                      {index + 1}
                    </div>
                    <div className="flex-1 bg-purple-50 p-6 rounded-2xl border-2 border-purple-200">
                      <h4 className="font-semibold text-purple-800 mb-2 text-lg">{step.title}</h4>
                      <p className="text-purple-600 mb-3">⏱️ Duration: {step.duration}</p>
                      
                      <div className="mb-4">
                        <h5 className="font-semibold text-purple-700 mb-2">🎯 Skills to Learn:</h5>
                        <div className="flex flex-wrap gap-2">
                          {step.skills.map((skill, skillIndex) => (
                            <span key={skillIndex} className="bg-white px-3 py-1 rounded-full text-sm text-purple-700 border border-purple-200">
                              {skill}
                            </span>
                          ))}
                        </div>
                      </div>

                      <div>
                        <h5 className="font-semibold text-purple-700 mb-2">📚 Learning Resources:</h5>
                        <div className="flex flex-wrap gap-2">
                          {step.resources.map((resource, resourceIndex) => (
                            <span key={resourceIndex} className="bg-yellow-100 px-3 py-1 rounded-full text-sm text-yellow-800 border border-yellow-200">
                              {resource}
                            </span>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>

              <div className="bg-gradient-to-r from-purple-500 to-pink-500 text-white p-6 rounded-2xl">
                <h4 className="font-semibold mb-3 text-lg">🚀 Next Steps to Success:</h4>
                <ul className="space-y-2">
                  {generatedRoadmap.nextSteps.map((step, index) => (
                    <li key={index} className="flex items-center gap-2">
                      <ChevronRight className="w-4 h-4" />
                      {step}
                    </li>
                  ))}
                </ul>
                <div className="mt-4 text-center">
                  <p className="text-lg font-semibold">Remember: Every expert was once a beginner! 💪✨</p>
                </div>
              </div>
            </div>
          ) : (
            <div className="bg-white rounded-3xl shadow-lg p-6 border-2 border-purple-200 text-center">
              <Map className="w-16 h-16 text-purple-400 mx-auto mb-4" />
              <h2 className="text-2xl font-bold text-purple-600 mb-4">Generate Your Personal Roadmap</h2>
              <p className="text-gray-600 mb-6">
                {selectedInterests.length > 0 
                  ? 'Click the button below to generate your personalized career roadmap!'
                  : 'First, go to "Choose Interests" to select what you\'re passionate about!'
                }
              </p>
              
              {selectedInterests.length > 0 ? (
                <button
                  onClick={generateRoadmap}
                  className="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-8 py-4 rounded-2xl font-semibold hover:shadow-lg transition-all text-lg"
                >
                  Generate My Roadmap! 🚀
                </button>
              ) : (
                <button
                  onClick={() => setCurrentStep('interests')}
                  className="bg-gradient-to-r from-purple-400 to-pink-400 text-white px-8 py-4 rounded-2xl font-semibold hover:shadow-lg transition-all text-lg"
                >
                  Choose My Interests First! ✨
                </button>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default AICareerCounselor;