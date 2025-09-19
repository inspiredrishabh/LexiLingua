import React, { useState } from 'react';
import { Upload, FileText, ArrowLeft, Globe, Zap, Shield, CheckCircle, Bot } from 'lucide-react';

const LexiLinguaUpload = () => {
  const [uploadHover, setUploadHover] = useState(false);
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [selectedFile, setSelectedFile] = useState(null);
  const [dragActive, setDragActive] = useState(false);

  // Theme classes
  const themeClasses = {
    mainBg: isDarkMode ? 'bg-gray-900' : 'bg-amber-50',
    cardBg: isDarkMode ? 'bg-gray-800' : 'bg-white',
    navBg: isDarkMode ? 'bg-gray-800 border-gray-700' : 'bg-yellow-100 border-amber-200',
    primaryText: isDarkMode ? 'text-white' : 'text-amber-900',
    secondaryText: isDarkMode ? 'text-gray-300' : 'text-amber-800',
    mutedText: isDarkMode ? 'text-gray-400' : 'text-amber-700',
    primaryBtn: isDarkMode ? 'bg-blue-600 hover:bg-blue-700' : 'bg-amber-800 hover:bg-amber-900',
    border: isDarkMode ? 'border-gray-600' : 'border-amber-300',
    uploadBg: isDarkMode ? 'bg-gray-700' : 'bg-yellow-50',
    uploadBorder: isDarkMode ? 'border-gray-500' : 'border-amber-400',
    iconBg: isDarkMode ? 'bg-gray-700' : 'bg-amber-800'
  };

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      setSelectedFile(e.dataTransfer.files[0]);
    }
  };

  const handleFileSelect = (e) => {
    if (e.target.files && e.target.files[0]) {
      setSelectedFile(e.target.files[0]);
    }
  };

  const goToDemo = () => {
    window.location.href = '/demo';
  };

  const goHome = () => {
    window.location.href = '/';
  };

  return (
    <div className={`min-h-screen ${themeClasses.mainBg} transition-colors duration-300`}>
      {/* Navigation */}
      <nav className={`${themeClasses.navBg} shadow-sm border-b transition-colors duration-300`}>
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <button 
                onClick={goHome}
                className={`p-2 rounded-lg ${themeClasses.border} border hover:bg-gray-100 transition-colors`}
              >
                <ArrowLeft className={`w-5 h-5 ${themeClasses.primaryText}`} />
              </button>
              <div className="flex items-center space-x-3">
                <div className={`w-10 h-10 ${themeClasses.iconBg} rounded-lg flex items-center justify-center`}>
                  <FileText className="w-6 h-6 text-white" />
                </div>
                <div>
                  <div className={`text-2xl font-bold ${themeClasses.primaryText}`}>LexiLingua</div>
                  <div className="flex items-center space-x-2">
                    <span className={`text-xs ${themeClasses.mutedText}`}>Powered by</span>
                    <Bot className={`w-4 h-4 ${themeClasses.secondaryText}`} />
                    <span className={`text-xs font-semibold ${themeClasses.secondaryText}`}>Gemini AI</span>
                  </div>
                </div>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <button 
                onClick={goToDemo}
                className={`px-4 py-2 rounded-lg ${themeClasses.border} border ${themeClasses.secondaryText} hover:bg-gray-50 transition-colors`}
              >
                View Demo
              </button>
            </div>
          </div>
        </div>
      </nav>

      <div className="max-w-4xl mx-auto px-6 py-12">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className={`text-4xl font-bold ${themeClasses.primaryText} mb-4`}>
            Upload Your Legal Document
          </h1>
          <p className={`text-xl ${themeClasses.mutedText} mb-6 max-w-2xl mx-auto`}>
            Get instant AI-powered analysis with risk assessment, plain-language summary, and interactive Q&A
          </p>
          <div className="flex items-center justify-center space-x-2 mb-8">
            <Bot className="w-5 h-5 text-blue-600" />
            <span className={`text-sm font-medium ${themeClasses.secondaryText}`}>
              Powered by Advanced Gemini AI Technology
            </span>
          </div>
        </div>

        {/* Upload Section */}
        <div className={`${themeClasses.cardBg} rounded-2xl shadow-lg p-8 mb-8 ${themeClasses.border} border`}>
          {/* Language Selection */}
          <div className="grid md:grid-cols-2 gap-6 mb-8">
            <div>
              <label className={`block text-sm font-medium ${themeClasses.primaryText} mb-3`}>
                1. What language is your document in?
              </label>
              <div className="space-y-3">
                <select className={`w-full p-4 border ${themeClasses.border} rounded-lg ${themeClasses.cardBg} ${themeClasses.primaryText} focus:ring-2 focus:ring-blue-500 focus:border-transparent text-base`}>
                  <option value="auto">🤖 Auto-Detect Language (Gemini AI)</option>
                  <option value="en">🇺🇸 English</option>
                  <option value="es">🇪🇸 Spanish</option>
                  <option value="fr">🇫🇷 French</option>
                  <option value="de">🇩🇪 German</option>
                  <option value="it">🇮🇹 Italian</option>
                  <option value="pt">🇵🇹 Portuguese</option>
                  <option value="ru">🇷🇺 Russian</option>
                  <option value="zh">🇨🇳 Chinese</option>
                  <option value="ja">🇯🇵 Japanese</option>
                  <option value="ar">🇸🇦 Arabic</option>
                  <option value="hi">🇮🇳 Hindi</option>
                </select>
                <div className={`p-3 ${isDarkMode ? 'bg-blue-900 border-blue-700 text-blue-300' : 'bg-blue-100 border-blue-400 text-blue-800'} border rounded-lg text-sm text-center font-medium`}>
                  ✨ Gemini AI-Powered Detection
                </div>
              </div>
            </div>

            <div>
              <label className={`block text-sm font-medium ${themeClasses.primaryText} mb-3`}>
                2. Which language would you like the analysis in?
              </label>
              <select className={`w-full p-4 border ${themeClasses.border} rounded-lg ${themeClasses.cardBg} ${themeClasses.primaryText} focus:ring-2 focus:ring-green-500 focus:border-transparent text-base`}>
                <option value="en">🇺🇸 English</option>
                <option value="es">🇪🇸 Spanish</option>
                <option value="fr">🇫🇷 French</option>
                <option value="de">🇩🇪 German</option>
                <option value="it">🇮🇹 Italian</option>
                <option value="pt">🇵🇹 Portuguese</option>
                <option value="ru">🇷🇺 Russian</option>
                <option value="zh">🇨🇳 Chinese</option>
                <option value="ja">🇯🇵 Japanese</option>
                <option value="ar">🇸🇦 Arabic</option>
                <option value="hi">🇮🇳 Hindi</option>
              </select>
            </div>
          </div>

          {/* File Upload Area */}
          <div 
            className={`relative border-2 border-dashed rounded-2xl p-12 text-center transition-all duration-300 cursor-pointer ${
              dragActive || uploadHover
                ? `${themeClasses.uploadBorder} bg-blue-50 border-blue-400`
                : `${themeClasses.border} ${themeClasses.uploadBg}`
            }`}
            onDragEnter={handleDrag}
            onDragLeave={handleDrag}
            onDragOver={handleDrag}
            onDrop={handleDrop}
            onMouseEnter={() => setUploadHover(true)}
            onMouseLeave={() => setUploadHover(false)}
          >
            <input
              type="file"
              accept=".pdf,.doc,.docx,.jpg,.jpeg,.png,.txt"
              onChange={handleFileSelect}
              className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
            />
            
            {selectedFile ? (
              <div className="space-y-4">
                <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto">
                  <CheckCircle className="w-8 h-8 text-green-600" />
                </div>
                <div>
                  <h3 className={`text-xl font-semibold ${themeClasses.primaryText} mb-2`}>
                    File Selected Successfully!
                  </h3>
                  <p className={`${themeClasses.mutedText} mb-2`}>
                    {selectedFile.name} ({(selectedFile.size / 1024 / 1024).toFixed(2)} MB)
                  </p>
                  <button 
                    onClick={() => setSelectedFile(null)}
                    className={`text-sm ${themeClasses.secondaryText} hover:underline`}
                  >
                    Choose different file
                  </button>
                </div>
              </div>
            ) : (
              <div className="space-y-4">
                <div className={`w-16 h-16 ${isDarkMode ? 'bg-gray-600' : 'bg-amber-200'} rounded-full flex items-center justify-center mx-auto`}>
                  <Upload className={`w-8 h-8 ${themeClasses.secondaryText}`} />
                </div>
                <div>
                  <h3 className={`text-xl font-semibold ${themeClasses.primaryText} mb-2`}>
                    Drop your file here or click to browse
                  </h3>
                  <p className={`${themeClasses.mutedText} mb-4`}>
                    Supports: PDF, DOC, DOCX, JPG, PNG, Handwritten documents
                  </p>
                  <p className={`text-sm ${themeClasses.mutedText}`}>
                    Maximum file size: 10MB
                  </p>
                </div>
              </div>
            )}
          </div>

          {/* Processing Features */}
          <div className="grid grid-cols-3 gap-4 mt-8">
            <div className={`${isDarkMode ? 'bg-green-900 border-green-700 text-green-300' : 'bg-green-100 border-green-400 text-green-800'} border p-4 rounded-lg text-center`}>
              <Shield className="w-6 h-6 mx-auto mb-2" />
              <div className="font-medium text-sm">Risk Analysis</div>
              <div className="text-xs opacity-80">AI-Powered</div>
            </div>
            <div className={`${isDarkMode ? 'bg-blue-900 border-blue-700 text-blue-300' : 'bg-blue-100 border-blue-400 text-blue-800'} border p-4 rounded-lg text-center`}>
              <FileText className="w-6 h-6 mx-auto mb-2" />
              <div className="font-medium text-sm">Plain Summary</div>
              <div className="text-xs opacity-80">Gemini AI</div>
            </div>
            <div className={`${isDarkMode ? 'bg-purple-900 border-purple-700 text-purple-300' : 'bg-purple-100 border-purple-400 text-purple-800'} border p-4 rounded-lg text-center`}>
              <Zap className="w-6 h-6 mx-auto mb-2" />
              <div className="font-medium text-sm">Next Steps</div>
              <div className="text-xs opacity-80">AI Guidance</div>
            </div>
          </div>

          {/* Action Button */}
          <div className="mt-8 text-center">
            <button 
              onClick={goToDemo}
              disabled={!selectedFile}
              className={`${themeClasses.primaryBtn} text-white px-8 py-4 rounded-lg font-semibold transition-all duration-300 shadow-lg text-lg flex items-center justify-center gap-3 mx-auto ${
                !selectedFile ? 'opacity-50 cursor-not-allowed' : 'hover:scale-105'
              }`}
            >
              <Bot className="w-6 h-6" />
              {selectedFile ? 'Analyze with Gemini AI' : 'Select a file to continue'}
              {selectedFile && <Zap className="w-6 h-6" />}
            </button>
            {selectedFile && (
              <p className={`text-sm ${themeClasses.mutedText} mt-3`}>
                Click to see a demo of the analysis process
              </p>
            )}
          </div>
        </div>

        {/* Security & Trust */}
        <div className={`${themeClasses.cardBg} rounded-xl p-6 ${themeClasses.border} border`}>
          <h3 className={`text-lg font-semibold ${themeClasses.primaryText} mb-4 text-center`}>
            Your Documents Are Secure
          </h3>
          <div className="grid md:grid-cols-3 gap-4 text-center">
            <div className={`p-4 rounded-lg ${themeClasses.uploadBg}`}>
              <Shield className={`w-8 h-8 ${themeClasses.secondaryText} mx-auto mb-2`} />
              <div className={`font-medium ${themeClasses.primaryText} text-sm`}>Bank-Grade Encryption</div>
              <div className={`text-xs ${themeClasses.mutedText}`}>256-bit SSL Security</div>
            </div>
            <div className={`p-4 rounded-lg ${themeClasses.uploadBg}`}>
              <Globe className={`w-8 h-8 ${themeClasses.secondaryText} mx-auto mb-2`} />
              <div className={`font-medium ${themeClasses.primaryText} text-sm`}>GDPR Compliant</div>
              <div className={`text-xs ${themeClasses.mutedText}`}>EU Privacy Standards</div>
            </div>
            <div className={`p-4 rounded-lg ${themeClasses.uploadBg}`}>
              <CheckCircle className={`w-8 h-8 ${themeClasses.secondaryText} mx-auto mb-2`} />
              <div className={`font-medium ${themeClasses.primaryText} text-sm`}>Auto-Delete</div>
              <div className={`text-xs ${themeClasses.mutedText}`}>Files removed after 24h</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LexiLinguaUpload;