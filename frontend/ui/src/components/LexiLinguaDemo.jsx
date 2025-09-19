import React, { useState, useEffect } from 'react';
import { FileText, AlertTriangle, CheckCircle, MessageSquare, Upload, Download, Copy, Share2, Bot, User, Shield, Scale, Clock, Eye } from 'lucide-react';

const LexiLinguaDemo = () => {
  const [currentStep, setCurrentStep] = useState(0);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [showResults, setShowResults] = useState(false);
  const [isDarkMode, setIsDarkMode] = useState(false);

  // Demo progression
  useEffect(() => {
    const timer = setTimeout(() => {
      if (currentStep === 0) {
        setCurrentStep(1);
        setIsAnalyzing(true);
      } else if (currentStep === 1) {
        setTimeout(() => {
          setIsAnalyzing(false);
          setShowResults(true);
          setCurrentStep(2);
        }, 3000);
      }
    }, 2000);

    return () => clearTimeout(timer);
  }, [currentStep]);

  // Theme classes
  const themeClasses = {
    mainBg: isDarkMode ? 'bg-gray-900' : 'bg-amber-50',
    cardBg: isDarkMode ? 'bg-gray-800' : 'bg-white',
    textPrimary: isDarkMode ? 'text-white' : 'text-gray-900',
    textSecondary: isDarkMode ? 'text-gray-300' : 'text-gray-700',
    textMuted: isDarkMode ? 'text-gray-400' : 'text-gray-500',
    border: isDarkMode ? 'border-gray-700' : 'border-gray-200',
    primaryBtn: isDarkMode ? 'bg-blue-600 hover:bg-blue-700' : 'bg-amber-600 hover:bg-amber-700',
  };

  const extractedText = `
EMPLOYMENT AGREEMENT

This Employment Agreement ("Agreement") is entered into on January 15, 2024, between TechCorp Solutions Inc., a Delaware corporation ("Company"), and John Smith ("Employee").

1. POSITION AND DUTIES
Employee shall serve as Senior Software Developer and shall perform such duties as are customarily associated with such position.

2. COMPENSATION
Company shall pay Employee a base salary of $85,000 per annum, payable in bi-weekly installments.

3. CONFIDENTIALITY AND NON-COMPETE
Employee agrees not to disclose any confidential information and shall not engage in any competing business for a period of 24 months following termination.

4. TERMINATION
Either party may terminate this agreement with 30 days written notice. Upon termination for cause, Company may terminate immediately without notice or severance pay.

5. GOVERNING LAW
This Agreement shall be governed by the laws of the State of Delaware.
  `;

  const aiAnalysis = {
    summary: "This is a standard employment agreement with several concerning clauses that heavily favor the employer. The contract includes restrictive non-compete terms and allows immediate termination without severance in certain circumstances.",
    riskLevel: "Medium-High",
    riskColor: "text-orange-600",
    riskBg: "bg-orange-100",
    keyFindings: [
      {
        type: "⚠️ High Risk",
        item: "24-month non-compete clause is unusually long and may limit future employment opportunities",
        color: "text-red-600 bg-red-50"
      },
      {
        type: "⚠️ Medium Risk", 
        item: "Termination 'for cause' allows immediate dismissal without severance pay",
        color: "text-orange-600 bg-orange-50"
      },
      {
        type: "✅ Standard",
        item: "30-day notice period for regular termination is reasonable",
        color: "text-green-600 bg-green-50"
      },
      {
        type: "✅ Fair",
        item: "Base salary of $85,000 is within market range for the position",
        color: "text-green-600 bg-green-50"
      }
    ],
    recommendations: [
      "Negotiate to reduce non-compete period from 24 months to 6-12 months",
      "Request definition of 'cause' for termination to be more specific",
      "Consider adding severance pay clause for termination without cause",
      "Clarify what constitutes 'confidential information'"
    ]
  };

  const qaSection = {
    question: "@gemini please explain the term 'non-compete clause'",
    answer: "A non-compete clause is a contractual agreement that prohibits an employee from working for competitors or starting a competing business for a specified period after leaving their current job. In your contract, this clause prevents you from engaging in any competing business for 24 months after termination. This is considered quite restrictive - typical non-compete periods range from 6-12 months. The 24-month duration could significantly limit your career opportunities and earning potential. I recommend negotiating this down to a shorter period, ideally 6-12 months, which is more reasonable and industry-standard."
  };

  return (
    <div className={`min-h-screen ${themeClasses.mainBg} transition-colors duration-300`}>
      {/* Header */}
      <header className={`${themeClasses.cardBg} shadow-sm border-b ${themeClasses.border} sticky top-0 z-50`}>
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-amber-600 rounded-lg flex items-center justify-center">
                <FileText className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className={`text-2xl font-bold ${themeClasses.textPrimary}`}>LexiLingua</h1>
                <p className={`text-sm ${themeClasses.textMuted}`}>AI-Powered Legal Document Analyzer</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <div className={`px-4 py-2 rounded-lg ${themeClasses.cardBg} ${themeClasses.border} border`}>
                <span className={`text-sm font-medium ${themeClasses.textSecondary}`}>Demo Mode</span>
              </div>
            </div>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-6 py-8">
        {/* Progress Steps */}
        <div className="mb-8">
          <div className="flex items-center justify-between max-w-3xl mx-auto">
            {['Upload Document', 'AI Analysis', 'Results & Q&A'].map((step, index) => (
              <div key={index} className="flex items-center">
                <div className={`w-10 h-10 rounded-full flex items-center justify-center border-2 transition-all duration-500 ${
                  index <= currentStep 
                    ? 'bg-amber-600 border-amber-600 text-white' 
                    : 'bg-gray-200 border-gray-300 text-gray-500'
                }`}>
                  {index + 1}
                </div>
                <span className={`ml-3 font-medium ${
                  index <= currentStep ? themeClasses.textPrimary : themeClasses.textMuted
                }`}>
                  {step}
                </span>
                {index < 2 && (
                  <div className={`w-20 h-0.5 mx-4 transition-all duration-500 ${
                    index < currentStep ? 'bg-amber-600' : 'bg-gray-300'
                  }`} />
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Step 1: Document Upload */}
        {currentStep >= 0 && (
          <div className={`${themeClasses.cardBg} rounded-xl shadow-lg p-6 mb-8 ${themeClasses.border} border`}>
            <div className="flex items-center mb-4">
              <Upload className={`w-6 h-6 ${themeClasses.textPrimary} mr-3`} />
              <h2 className={`text-xl font-bold ${themeClasses.textPrimary}`}>Document Upload Complete</h2>
              <CheckCircle className="w-5 h-5 text-green-600 ml-3" />
            </div>
            <div className={`p-4 rounded-lg ${themeClasses.border} border-dashed`}>
              <div className="flex items-center justify-between">
                <div className="flex items-center">
                  <FileText className={`w-8 h-8 ${themeClasses.textSecondary} mr-3`} />
                  <div>
                    <p className={`font-medium ${themeClasses.textPrimary}`}>employment_agreement.pdf</p>
                    <p className={`text-sm ${themeClasses.textMuted}`}>1.2 MB • Uploaded successfully</p>
                  </div>
                </div>
                <div className="flex space-x-2">
                  <button className={`p-2 rounded-lg ${themeClasses.border} border hover:bg-gray-50 transition-colors`}>
                    <Eye className={`w-4 h-4 ${themeClasses.textSecondary}`} />
                  </button>
                  <button className={`p-2 rounded-lg ${themeClasses.border} border hover:bg-gray-50 transition-colors`}>
                    <Download className={`w-4 h-4 ${themeClasses.textSecondary}`} />
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Step 2: AI Analysis Loading */}
        {isAnalyzing && (
          <div className={`${themeClasses.cardBg} rounded-xl shadow-lg p-6 mb-8 ${themeClasses.border} border`}>
            <div className="text-center py-8">
              <div className="w-16 h-16 mx-auto mb-4 bg-blue-100 rounded-full flex items-center justify-center">
                <Bot className="w-8 h-8 text-blue-600 animate-pulse" />
              </div>
              <h3 className={`text-xl font-bold ${themeClasses.textPrimary} mb-2`}>AI Analysis in Progress</h3>
              <p className={`${themeClasses.textMuted} mb-4`}>Analyzing document content, identifying risks, and preparing insights...</p>
              <div className="max-w-md mx-auto bg-gray-200 rounded-full h-2">
                <div className="bg-blue-600 h-2 rounded-full animate-pulse" style={{width: '75%'}}></div>
              </div>
            </div>
          </div>
        )}

        {/* Step 3: Results */}
        {showResults && (
          <>
            {/* Extracted Text */}
            <div className={`${themeClasses.cardBg} rounded-xl shadow-lg p-6 mb-8 ${themeClasses.border} border`}>
              <div className="flex items-center justify-between mb-4">
                <h2 className={`text-xl font-bold ${themeClasses.textPrimary} flex items-center`}>
                  <FileText className="w-6 h-6 mr-3" />
                  Extracted Text
                </h2>
                <button className={`px-4 py-2 rounded-lg ${themeClasses.border} border hover:bg-gray-50 transition-colors flex items-center`}>
                  <Copy className={`w-4 h-4 mr-2 ${themeClasses.textSecondary}`} />
                  <span className={`text-sm ${themeClasses.textSecondary}`}>Copy</span>
                </button>
              </div>
              <div className={`p-4 rounded-lg bg-gray-50 ${themeClasses.border} border max-h-64 overflow-y-auto`}>
                <pre className={`text-sm ${themeClasses.textSecondary} whitespace-pre-wrap font-mono`}>
                  {extractedText}
                </pre>
              </div>
            </div>

            {/* AI Analysis */}
            <div className={`${themeClasses.cardBg} rounded-xl shadow-lg p-6 mb-8 ${themeClasses.border} border`}>
              <div className="flex items-center mb-6">
                <Bot className={`w-6 h-6 ${themeClasses.textPrimary} mr-3`} />
                <h2 className={`text-xl font-bold ${themeClasses.textPrimary}`}>AI Analysis</h2>
              </div>

              {/* Risk Level */}
              <div className={`p-4 rounded-lg ${aiAnalysis.riskBg} border border-orange-200 mb-6`}>
                <div className="flex items-center">
                  <AlertTriangle className={`w-6 h-6 ${aiAnalysis.riskColor} mr-3`} />
                  <div>
                    <h3 className={`font-bold ${aiAnalysis.riskColor}`}>Risk Level: {aiAnalysis.riskLevel}</h3>
                    <p className="text-orange-700 text-sm">{aiAnalysis.summary}</p>
                  </div>
                </div>
              </div>

              {/* Key Findings */}
              <div className="mb-6">
                <h3 className={`text-lg font-semibold ${themeClasses.textPrimary} mb-4`}>Key Findings</h3>
                <div className="space-y-3">
                  {aiAnalysis.keyFindings.map((finding, index) => (
                    <div key={index} className={`p-3 rounded-lg ${finding.color.split(' ')[1]} border`}>
                      <div className="flex items-start">
                        <span className={`font-medium ${finding.color.split(' ')[0]} mr-3`}>{finding.type}</span>
                        <p className={`${finding.color.split(' ')[0]} text-sm`}>{finding.item}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Recommendations */}
              <div>
                <h3 className={`text-lg font-semibold ${themeClasses.textPrimary} mb-4`}>Recommendations</h3>
                <div className="space-y-2">
                  {aiAnalysis.recommendations.map((rec, index) => (
                    <div key={index} className="flex items-start">
                      <CheckCircle className="w-5 h-5 text-blue-600 mr-3 mt-0.5 flex-shrink-0" />
                      <p className={`text-sm ${themeClasses.textSecondary}`}>{rec}</p>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Q&A Section */}
            <div className={`${themeClasses.cardBg} rounded-xl shadow-lg p-6 ${themeClasses.border} border`}>
              <div className="flex items-center mb-6">
                <MessageSquare className={`w-6 h-6 ${themeClasses.textPrimary} mr-3`} />
                <h2 className={`text-xl font-bold ${themeClasses.textPrimary}`}>Interactive Q&A</h2>
              </div>

              {/* Question */}
              <div className="mb-4">
                <div className="flex items-start mb-3">
                  <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center mr-3">
                    <User className="w-4 h-4 text-white" />
                  </div>
                  <div className="flex-1">
                    <div className={`p-3 rounded-lg bg-blue-50 border border-blue-200`}>
                      <p className={`text-sm ${themeClasses.textPrimary}`}>{qaSection.question}</p>
                    </div>
                  </div>
                </div>
              </div>

              {/* Answer */}
              <div className="mb-4">
                <div className="flex items-start">
                  <div className="w-8 h-8 bg-amber-600 rounded-full flex items-center justify-center mr-3">
                    <Bot className="w-4 h-4 text-white" />
                  </div>
                  <div className="flex-1">
                    <div className={`p-4 rounded-lg bg-amber-50 border border-amber-200`}>
                      <p className={`text-sm ${themeClasses.textSecondary} leading-relaxed`}>{qaSection.answer}</p>
                    </div>
                  </div>
                </div>
              </div>

              {/* Input for new question */}
              <div className="mt-6 p-4 rounded-lg bg-gray-50 border-2 border-dashed border-gray-300">
                <div className="flex items-center">
                  <input 
                    type="text" 
                    placeholder="Ask another question about your document..."
                    className="flex-1 p-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                  <button className={`ml-3 ${themeClasses.primaryBtn} text-white px-6 py-3 rounded-lg font-medium transition-colors`}>
                    Ask
                  </button>
                </div>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="mt-8 flex items-center justify-center space-x-4">
              <button className={`${themeClasses.primaryBtn} text-white px-8 py-3 rounded-lg font-semibold transition-colors flex items-center`}>
                <Download className="w-5 h-5 mr-2" />
                Download Report
              </button>
              <button className={`px-8 py-3 rounded-lg border-2 ${themeClasses.border} ${themeClasses.textPrimary} hover:bg-gray-50 transition-colors flex items-center`}>
                <Share2 className="w-5 h-5 mr-2" />
                Share Analysis
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default LexiLinguaDemo;