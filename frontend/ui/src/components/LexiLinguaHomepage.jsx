import React, { useState } from 'react';
import { Upload, FileText, Shield, Globe, CheckCircle, ArrowRight, Zap, Eye, MessageSquare, Scale, Lock, Award, Sun, Moon } from 'lucide-react';

const LexiLinguaHomepage = () => {
  const [uploadHover, setUploadHover] = useState(false);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
  };

  const features = [
    {
      icon: <FileText className="w-8 h-8" />,
      title: "Processes Handwritten Documents",
      description: "Our cutting-edge OCR is designed to read scanned handwritten text correctly—a huge hurdle where the majority of digital tools don't stand a chance.",
      lightColor: "bg-blue-700",
      darkColor: "bg-blue-600"
    },
    {
      icon: <Globe className="w-8 h-8" />,
      title: "Better Cross-Language Analysis",
      description: "Contrary to simple translators that lack legal subtlety, our AI is trained to interpret legal meaning and intent, not simply words.",
      lightColor: "bg-green-700",
      darkColor: "bg-green-600"
    },
    {
      icon: <Shield className="w-8 h-8" />,
      title: "Law-Specific Legal Insights",
      description: "We offer targeted risk analysis and clause deconstruction, far beyond generic AI summarizers that lack legal context understanding.",
      lightColor: "bg-red-700",
      darkColor: "bg-red-600"
    },
    {
      icon: <Zap className="w-8 h-8" />,
      title: "Instant & Accessible",
      description: "We provide an instant, low-cost initial review, avoiding the expense and wait involved with conventional legal advice.",
      lightColor: "bg-indigo-700",
      darkColor: "bg-indigo-600"
    }
  ];

  const uspPillars = [
    {
      icon: <Eye className="w-12 h-12" />,
      title: "Analyze the \"Impossible\" Document",
      description: "The only platform engineered to handle complex handwritten notes and foreign language contracts. If you can scan it, we can interpret its legal intent."
    },
    {
      icon: <MessageSquare className="w-12 h-12" />,
      title: "Go Beyond Static Summaries",
      description: "Our interactive Q&A allows you to \"talk\" to your document, providing deep contextual understanding of legal nuances."
    },
    {
      icon: <CheckCircle className="w-12 h-12" />,
      title: "Deliver an Actionable Plan",
      description: "Get a clear \"Next Steps\" checklist after analysis, bridging the gap between understanding and action."
    }
  ];

  const benefits = [
    "Empowers you by breaking down complex legal language into plain, simple words",
    "Demolishes language barriers by examining documents in any language and returning insights in your preferred language",
    "Identifies hidden risks and predatory clauses prior to signing, serving as a vital security net",
    "Creates a clear 'Next Steps' checklist to lead users from confusion to completion"
  ];

  const trustIndicators = [
    { icon: <Lock className="w-6 h-6" />, text: "Bank-Grade Security" },
    { icon: <Award className="w-6 h-6" />, text: "Certified Legal AI" },
    { icon: <Scale className="w-6 h-6" />, text: "Compliance Ready" }
  ];

  // Theme classes
  const themeClasses = {
    // Main backgrounds
    mainBg: isDarkMode ? 'bg-gray-900' : 'bg-amber-50',
    cardBg: isDarkMode ? 'bg-gray-800' : 'bg-yellow-50',
    navBg: isDarkMode ? 'bg-gray-800 border-gray-700' : 'bg-yellow-100 border-amber-200',
    sectionBg: isDarkMode ? 'bg-gray-800' : 'bg-amber-100',
    footerBg: isDarkMode ? 'bg-gray-900 border-gray-700' : 'bg-amber-900 border-amber-800',
    
    // Text colors
    primaryText: isDarkMode ? 'text-white' : 'text-amber-900',
    secondaryText: isDarkMode ? 'text-gray-300' : 'text-amber-800',
    mutedText: isDarkMode ? 'text-gray-400' : 'text-amber-700',
    
    // Buttons and accents
    primaryBtn: isDarkMode ? 'bg-blue-600 hover:bg-blue-700' : 'bg-amber-800 hover:bg-amber-900',
    secondaryBtn: isDarkMode ? 'border-gray-600 text-gray-300 hover:border-gray-500 hover:bg-gray-700' : 'border-amber-600 text-amber-800 hover:border-amber-700 hover:bg-amber-200',
    
    // Borders and dividers
    border: isDarkMode ? 'border-gray-600' : 'border-amber-300',
    borderHover: isDarkMode ? 'hover:border-gray-500' : 'hover:border-amber-400',
    
    // Special elements
    uploadBg: isDarkMode ? 'bg-gray-700' : 'bg-yellow-50',
    uploadBorder: isDarkMode ? 'border-gray-500' : 'border-amber-400',
    iconBg: isDarkMode ? 'bg-gray-700' : 'bg-amber-800'
  };

  return (
    <div className={`min-h-screen ${themeClasses.mainBg} transition-colors duration-300`}>
      {/* Navigation */}
      <nav className={`${themeClasses.navBg} shadow-sm border-b transition-colors duration-300`}>
        <div className="max-w-full mx-auto px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className={`w-10 h-10 ${themeClasses.iconBg} rounded-lg flex items-center justify-center`}>
                <FileText className="w-6 h-6 text-white" />
              </div>
              <div className={`text-2xl font-bold ${themeClasses.primaryText}`}>
                LexiLingua
              </div>
            </div>
            <div className={`hidden md:flex space-x-8 ${themeClasses.mutedText}`}>
              <a href="#features" className={`hover:${themeClasses.primaryText.split(' ')[0]} transition-colors font-medium`}>Features</a>
              <a href="#how-it-works" className={`hover:${themeClasses.primaryText.split(' ')[0]} transition-colors font-medium`}>How It Works</a>
              <a href="#pricing" className={`hover:${themeClasses.primaryText.split(' ')[0]} transition-colors font-medium`}>Pricing</a>
            </div>
            <div className="flex items-center space-x-4">
              <button
                onClick={toggleTheme}
                className={`p-2 rounded-lg ${themeClasses.cardBg} ${themeClasses.border} border hover:scale-105 transition-all`}
                aria-label="Toggle theme"
              >
                {isDarkMode ? (
                  <Sun className={`w-5 h-5 ${themeClasses.primaryText}`} />
                ) : (
                  <Moon className={`w-5 h-5 ${themeClasses.primaryText}`} />
                )}
              </button>
              <button className={`${themeClasses.primaryBtn} text-white px-6 py-2 rounded-lg transition-colors font-medium`}>
                Get Started
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className={`${themeClasses.cardBg} px-8 py-12 transition-colors duration-300`}>
        <div className="max-w-full mx-auto px-4">
          <div className="text-center lg:text-left max-w-6xl mx-auto">
            <h1 className={`text-3xl lg:text-4xl font-bold ${themeClasses.primaryText} mb-3 leading-tight`}>
              Transform Complex Legal Documents
              <span className={`block ${themeClasses.secondaryText} text-xl lg:text-2xl font-medium mt-1`}>
                Professional Analysis & Verification
              </span>
            </h1>
            <p className={`text-lg ${themeClasses.mutedText} mb-4 leading-relaxed`}>
              LexiLingua is an artificial intelligence platform that simplifies complex legal documents into clear, actionable information in your preferred language. Created for ordinary citizens, freelancers, and small business owners who need legal clarity without expensive lawyers.
            </p>
            <div className={`${isDarkMode ? 'bg-gray-700' : 'bg-amber-200'} rounded-lg p-3 mb-4`}>
              <p className={`text-base ${themeClasses.primaryText} font-medium`}>
                ✨ Get instant detailed reports with summary, risk rating, and interactive Q&A to make confident decisions with full information.
              </p>
            </div>
            
            {/* Trust Indicators */}
            <div className="flex flex-wrap gap-4 justify-center items-center mb-6">
              {trustIndicators.map((indicator, index) => (
                <div key={index} className={`flex items-center gap-2 ${themeClasses.mutedText}`}>
                  <div className={themeClasses.secondaryText}>
                    {indicator.icon}
                  </div>
                  <span className="font-medium">{indicator.text}</span>
                </div>
              ))}
            </div>
            
            <div className="flex flex-col sm:flex-row gap-3 justify-center items-center mb-8">
              <button className={`${themeClasses.primaryBtn} text-white px-6 py-3 rounded-lg font-semibold transition-colors shadow-lg text-base`}>
                Upload Document Now
              </button>
              <button className={`border-2 ${themeClasses.secondaryBtn} px-6 py-3 rounded-lg font-semibold transition-colors text-base`}>
                See How It Works
              </button>
            </div>
          </div>
          
          {/* Enhanced Upload Section - Now Below Content */}
          <div className="max-w-6xl mx-auto mt-8">
            <div 
              className={`relative ${themeClasses.uploadBg} border-2 border-dashed rounded-2xl p-8 transition-all duration-300 shadow-lg ${uploadHover ? `${themeClasses.uploadBorder} shadow-xl` : `${themeClasses.border}`}`}
              onMouseEnter={() => setUploadHover(true)}
              onMouseLeave={() => setUploadHover(false)}
            >
              <div className="text-center mb-6">
                <div className={`w-16 h-16 ${isDarkMode ? 'bg-gray-600' : 'bg-amber-200'} rounded-full flex items-center justify-center mx-auto mb-4`}>
                  <Upload className={`w-8 h-8 ${themeClasses.secondaryText}`} />
                </div>
                <h3 className={`text-xl font-semibold ${themeClasses.primaryText} mb-2`}>Upload Your Legal Document</h3>
                <p className={`${themeClasses.mutedText} mb-4`}>PDF, Image, Handwritten - All formats supported</p>
              </div>

              {/* Language Selection Section */}
              <div className="grid md:grid-cols-2 gap-6 mb-6">
                <div>
                  <label className={`block text-sm font-medium ${themeClasses.primaryText} mb-2`}>
                    1. What language is your document in?
                  </label>
                  <div className="space-y-3">
                    <select className={`w-full p-3 border ${themeClasses.border} rounded-lg ${themeClasses.cardBg} ${themeClasses.primaryText} focus:ring-2 focus:ring-blue-500 focus:border-transparent`}>
                      <option value="auto">🤖 Auto-Detect Language</option>
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
                      ✨ AI-Powered Detection
                    </div>
                  </div>
                </div>

                <div>
                  <label className={`block text-sm font-medium ${themeClasses.primaryText} mb-2`}>
                    2. Which language would you like the analysis in?
                  </label>
                  <select className={`w-full p-3 border ${themeClasses.border} rounded-lg ${themeClasses.cardBg} ${themeClasses.primaryText} focus:ring-2 focus:ring-green-500 focus:border-transparent`}>
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

              {/* Upload Button */}
              <div className={`border-2 border-dashed ${themeClasses.border} rounded-xl p-8 mb-6 hover:${themeClasses.borderHover} transition-colors cursor-pointer`}>
                <div className="text-center">
                  <FileText className={`w-16 h-16 ${themeClasses.mutedText} mx-auto mb-3`} />
                  <p className={`${themeClasses.primaryText} font-medium mb-2 text-lg`}>Drop your file here or click to browse</p>
                  <p className={`${themeClasses.mutedText} text-sm`}>Supports: PDF, DOC, JPG, PNG, Handwritten documents</p>
                </div>
              </div>

              {/* Processing Features */}
              <div className="grid grid-cols-3 gap-3">
                <div className={`${isDarkMode ? 'bg-green-900 border-green-700 text-green-300' : 'bg-green-100 border-green-400 text-green-800'} border px-4 py-3 rounded-lg text-sm font-medium text-center`}>
                  ✓ Risk Analysis
                </div>
                <div className={`${isDarkMode ? 'bg-blue-900 border-blue-700 text-blue-300' : 'bg-blue-100 border-blue-400 text-blue-800'} border px-4 py-3 rounded-lg text-sm font-medium text-center`}>
                  ✓ Plain Summary
                </div>
                <div className={`${isDarkMode ? 'bg-purple-900 border-purple-700 text-purple-300' : 'bg-purple-100 border-purple-400 text-purple-800'} border px-4 py-3 rounded-lg text-sm font-medium text-center`}>
                  ✓ Next Steps
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className={`px-8 py-20 ${themeClasses.sectionBg} transition-colors duration-300`}>
        <div className="max-w-full mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className={`text-4xl font-bold ${themeClasses.primaryText} mb-6`}>What Makes LexiLingua Different</h2>
            <p className={`text-xl ${themeClasses.mutedText} max-w-5xl mx-auto`}>
              Unlike simple translators that lack legal subtlety or generic AI summarizers without legal context, our platform provides comprehensive legal understanding
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => (
              <div key={index} className="group">
                <div className={`${themeClasses.cardBg} ${themeClasses.border} border rounded-xl p-6 h-full hover:shadow-lg transition-all duration-300 ${themeClasses.borderHover}`}>
                  <div className={`w-16 h-16 ${isDarkMode ? feature.darkColor : feature.lightColor} rounded-lg flex items-center justify-center mb-4 group-hover:scale-105 transition-transform`}>
                    <div className="text-white">
                      {feature.icon}
                    </div>
                  </div>
                  <h3 className={`text-xl font-semibold ${themeClasses.primaryText} mb-3`}>{feature.title}</h3>
                  <p className={`${themeClasses.mutedText} leading-relaxed`}>{feature.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* USP Section */}
      <section className={`px-8 py-20 ${themeClasses.cardBg} transition-colors duration-300`}>
        <div className="max-w-full mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className={`text-4xl font-bold ${themeClasses.primaryText} mb-6`}>Complete Document Understanding</h2>
            <p className={`text-xl ${themeClasses.mutedText} max-w-3xl mx-auto`}>
              Our comprehensive approach delivers insights that basic document scanners and translators cannot match
            </p>
          </div>
          
          <div className="space-y-12">
            {uspPillars.map((pillar, index) => (
              <div key={index} className="group">
                <div className={`${themeClasses.sectionBg} ${themeClasses.border} border rounded-2xl p-8 hover:shadow-lg transition-all duration-300`}>
                  <div className="flex flex-col md:flex-row items-center gap-8">
                    <div className="flex-shrink-0">
                      <div className={`w-24 h-24 ${themeClasses.iconBg} rounded-full flex items-center justify-center text-white group-hover:scale-105 transition-transform`}>
                        {pillar.icon}
                      </div>
                    </div>
                    <div className="flex-1 text-center md:text-left">
                      <h3 className={`text-2xl font-bold ${themeClasses.primaryText} mb-4`}>{pillar.title}</h3>
                      <p className={`text-lg ${themeClasses.mutedText} leading-relaxed`}>{pillar.description}</p>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Benefits Section */}
      <section className={`px-8 py-20 ${themeClasses.sectionBg} transition-colors duration-300`}>
        <div className="max-w-full mx-auto px-4">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className={`text-4xl font-bold ${themeClasses.primaryText} mb-8`}>How We Solve Your Legal Document Challenges</h2>
              <div className="space-y-6">
                {benefits.map((benefit, index) => (
                  <div key={index} className="flex items-start gap-4 group">
                    <div className={`flex-shrink-0 w-8 h-8 ${isDarkMode ? 'bg-green-600' : 'bg-green-700'} rounded-full flex items-center justify-center group-hover:scale-110 transition-transform`}>
                      <CheckCircle className="w-5 h-5 text-white" />
                    </div>
                    <p className={`text-lg ${themeClasses.secondaryText} leading-relaxed`}>{benefit}</p>
                  </div>
                ))}
              </div>
            </div>
            
            <div className="relative">
              <div className={`${themeClasses.cardBg} ${themeClasses.border} border rounded-2xl p-8 shadow-lg`}>
                <h3 className={`text-2xl font-bold ${themeClasses.primaryText} mb-6`}>Start Your Document Analysis</h3>
                <p className={`${themeClasses.mutedText} mb-6`}>
                  Join thousands of professionals who trust LexiLingua for accurate legal document analysis and verification.
                </p>
                <div className="space-y-4">
                  <div className={`flex items-center gap-3 ${themeClasses.mutedText}`}>
                    <div className={`w-6 h-6 ${isDarkMode ? 'bg-green-800' : 'bg-green-200'} rounded-full flex items-center justify-center`}>
                      <div className={`w-2 h-2 ${isDarkMode ? 'bg-green-400' : 'bg-green-700'} rounded-full`}></div>
                    </div>
                    <span>Upload any document format</span>
                  </div>
                  <div className={`flex items-center gap-3 ${themeClasses.mutedText}`}>
                    <div className={`w-6 h-6 ${isDarkMode ? 'bg-green-800' : 'bg-green-200'} rounded-full flex items-center justify-center`}>
                      <div className={`w-2 h-2 ${isDarkMode ? 'bg-green-400' : 'bg-green-700'} rounded-full`}></div>
                    </div>
                    <span>Get instant professional analysis</span>
                  </div>
                  <div className={`flex items-center gap-3 ${themeClasses.mutedText}`}>
                    <div className={`w-6 h-6 ${isDarkMode ? 'bg-green-800' : 'bg-green-200'} rounded-full flex items-center justify-center`}>
                      <div className={`w-2 h-2 ${isDarkMode ? 'bg-green-400' : 'bg-green-700'} rounded-full`}></div>
                    </div>
                    <span>Receive clear action steps</span>
                  </div>
                </div>
                <button className={`w-full ${themeClasses.primaryBtn} text-white py-4 rounded-lg font-semibold transition-colors shadow-lg flex items-center justify-center gap-2 mt-6`}>
                  Begin Analysis
                  <ArrowRight className="w-5 h-5" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className={`px-8 py-20 ${themeClasses.iconBg} transition-colors duration-300`}>
        <div className="max-w-5xl mx-auto text-center">
          <h2 className="text-4xl font-bold text-white mb-6">
            Professional Legal Document Analysis Made Simple
          </h2>
          <p className={`text-xl ${isDarkMode ? 'text-gray-300' : 'text-amber-200'} mb-8`}>
            Don't let complex legal language create risks for your business. 
            Get professional-grade analysis in minutes, not days.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button className={`${isDarkMode ? 'bg-white text-gray-800 hover:bg-gray-100' : 'bg-amber-100 text-amber-900 hover:bg-amber-200'} px-12 py-4 rounded-lg font-semibold transition-colors shadow-lg text-lg`}>
              Upload Your Document
            </button>
            <button className={`border-2 ${isDarkMode ? 'border-gray-400 text-white hover:border-gray-300 hover:bg-gray-700' : 'border-amber-300 text-white hover:border-amber-200 hover:bg-amber-800'} px-12 py-4 rounded-lg font-semibold transition-colors text-lg`}>
              Schedule Demo
            </button>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className={`px-8 py-12 ${themeClasses.footerBg} border-t transition-colors duration-300`}>
        <div className="max-w-full mx-auto px-4">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-3 mb-4">
                <div className={`w-8 h-8 ${isDarkMode ? 'bg-gray-600' : 'bg-amber-700'} rounded-lg flex items-center justify-center`}>
                  <FileText className="w-5 h-5 text-white" />
                </div>
                <div className={`text-xl font-bold ${isDarkMode ? 'text-white' : 'text-amber-100'}`}>LexiLingua</div>
              </div>
              <p className={`${isDarkMode ? 'text-gray-400' : 'text-amber-300'}`}>
                Professional legal document analysis for businesses and individuals worldwide.
              </p>
            </div>
            <div>
              <h4 className={`font-semibold ${isDarkMode ? 'text-white' : 'text-amber-100'} mb-4`}>Product</h4>
              <div className={`space-y-2 ${isDarkMode ? 'text-gray-400' : 'text-amber-300'}`}>
                <div className={`${isDarkMode ? 'hover:text-white' : 'hover:text-amber-200'} cursor-pointer`}>Features</div>
                <div className={`${isDarkMode ? 'hover:text-white' : 'hover:text-amber-200'} cursor-pointer`}>Pricing</div>
                <div className={`${isDarkMode ? 'hover:text-white' : 'hover:text-amber-200'} cursor-pointer`}>API Access</div>
                <div className={`${isDarkMode ? 'hover:text-white' : 'hover:text-amber-200'} cursor-pointer`}>Enterprise</div>
              </div>
            </div>
            <div>
              <h4 className={`font-semibold ${isDarkMode ? 'text-white' : 'text-amber-100'} mb-4`}>Support</h4>
              <div className={`space-y-2 ${isDarkMode ? 'text-gray-400' : 'text-amber-300'}`}>
                <div className={`${isDarkMode ? 'hover:text-white' : 'hover:text-amber-200'} cursor-pointer`}>Help Center</div>
                <div className={`${isDarkMode ? 'hover:text-white' : 'hover:text-amber-200'} cursor-pointer`}>Contact Support</div>
                <div className={`${isDarkMode ? 'hover:text-white' : 'hover:text-amber-200'} cursor-pointer`}>Privacy Policy</div>
                <div className={`${isDarkMode ? 'hover:text-white' : 'hover:text-amber-200'} cursor-pointer`}>Terms of Service</div>
              </div>
            </div>
            <div>
              <h4 className={`font-semibold ${isDarkMode ? 'text-white' : 'text-amber-100'} mb-4`}>Company</h4>
              <div className={`space-y-2 ${isDarkMode ? 'text-gray-400' : 'text-amber-300'}`}>
                <div className={`${isDarkMode ? 'hover:text-white' : 'hover:text-amber-200'} cursor-pointer`}>About Us</div>
                <div className={`${isDarkMode ? 'hover:text-white' : 'hover:text-amber-200'} cursor-pointer`}>Blog</div>
                <div className={`${isDarkMode ? 'hover:text-white' : 'hover:text-amber-200'} cursor-pointer`}>Careers</div>
                <div className={`${isDarkMode ? 'hover:text-white' : 'hover:text-amber-200'} cursor-pointer`}>Press Kit</div>
              </div>
            </div>
          </div>
          <div className={`border-t ${isDarkMode ? 'border-gray-700' : 'border-amber-800'} mt-12 pt-8 text-center ${isDarkMode ? 'text-gray-400' : 'text-amber-300'}`}>
            <p>&copy; 2025 LexiLingua. All rights reserved. Professional legal document analysis platform.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LexiLinguaHomepage;