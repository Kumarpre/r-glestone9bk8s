import { useState, useRef, useEffect } from 'react';

function App() {
  const [messages, setMessages] = useState([
    {
      role: 'bot',
      content: 'Hi! I am the Mutual Fund FAQ Assistant. I can provide factual information about 5 HDFC schemes:\n- Mid Cap\n- Small Cap\n- Large Cap\n- Gold ETF\n- ELSS Tax Saver\n\nWhat would you like to know?',
      category: 'GREETING'
    }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const exampleQueries = [
    "What is the expense ratio of HDFC Small Cap?",
    "Tell me the exit load for the Gold ETF.",
    "Does the ELSS tax saver fund have a lock-in period?",
    "What is the minimum SIP for Large Cap?",
    "Show me the riskometer for Mid Cap."
  ];

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleSend = async (query) => {
    if (!query.trim()) return;
    
    const userMsg = { role: 'user', content: query };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8080/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
      });
      
      if (!response.ok) throw new Error('Network response was not ok');
      
      const data = await response.json();
      setMessages(prev => [...prev, {
        role: 'bot',
        content: data.answer,
        category: data.category
      }]);
    } catch (error) {
      console.error(error);
      setMessages(prev => [...prev, {
        role: 'bot',
        content: 'Sorry, I am having trouble connecting to the server. Please make sure the backend is running on port 8080.',
        category: 'ERROR'
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  const renderMessageContent = (text) => {
    // Basic Markdown/URL parser
    const urlRegex = /(https?:\/\/[^\s]+)/g;
    const parts = text.split(urlRegex);
    
    // Check if the text contains list items (e.g. from the greeting)
    if (text.includes('- ')) {
        const lines = text.split('\n');
        return lines.map((line, idx) => {
            if (line.trim().startsWith('- ')) {
                return <li key={idx} className="ml-4 list-disc text-on-surface-variant mb-1">{line.substring(2)}</li>
            }
            return <p key={idx} className="mb-2">{line}</p>
        });
    }

    return (
        <p>
            {parts.map((part, index) => {
            if (part.match(urlRegex)) {
                return (
                    <span key={index} className="mt-3 pt-3 border-t border-outline-variant/20 block">
                        <a 
                            className="text-primary hover:text-primary-fixed-dim transition-colors flex items-center gap-1 font-label-md text-label-md inline-flex" 
                            href={part} 
                            target="_blank" 
                            rel="noopener noreferrer"
                        >
                            <span className="material-symbols-outlined text-sm">open_in_new</span>
                            View Source
                        </a>
                    </span>
                );
            }
            return part;
            })}
        </p>
    );
  };

  return (
    <div className="bg-background text-on-surface ambient-bg min-h-screen flex flex-col font-body-md text-body-md overflow-hidden selection:bg-primary-container selection:text-on-primary">
      {/* TopAppBar */}
      <header className="flex justify-between items-center px-container-padding h-16 w-full z-50 fixed top-0 bg-surface/80 dark:bg-surface/80 backdrop-blur-xl border-b border-outline-variant/20 shadow-sm transition-all duration-300 ease-spring">
        <div className="flex items-center gap-3">
          <span className="material-symbols-outlined text-primary text-2xl" style={{ fontVariationSettings: "'FILL' 1" }}>assured_workload</span>
          <h1 className="font-headline-md text-headline-md font-semibold text-primary">Mutual Fund Assistant</h1>
        </div>
        <div className="hidden md:flex">
          {/* Disclaimer Pill */}
          <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-surface-container-high border border-outline-variant/30 font-label-md text-label-md text-on-surface-variant">
            <span className="material-symbols-outlined text-sm">info</span>
            <span>Facts-only. No investment advice.</span>
          </div>
        </div>
      </header>

      {/* Main Chat Layout */}
      <main className="flex-1 w-full max-w-max-width mx-auto flex flex-col pt-20 pb-4 relative h-screen">
        
        {/* Chat Canvas */}
        <div className="flex-1 w-full md:w-2/3 lg:w-[60%] mx-auto flex flex-col px-4 md:px-0 overflow-y-auto pb-40" id="chat-container">
          {/* Date Divider */}
          <div className="w-full flex justify-center my-6">
            <span className="font-label-md text-label-md text-outline-variant bg-surface-container-low px-3 py-1 rounded-full border border-outline-variant/10">Today</span>
          </div>

          {messages.map((msg, index) => (
            <div 
                key={index} 
                className={`flex w-full mb-6 animate-message opacity-0 ${msg.role === 'user' ? 'justify-end' : ''}`}
                style={{ animationDelay: '0.1s', animationFillMode: 'forwards' }}
            >
                {msg.role === 'bot' && (
                    <div className="flex-shrink-0 mr-3 mt-1">
                        <div className="w-8 h-8 rounded-full bg-surface-container-highest flex items-center justify-center border border-primary/20 text-primary">
                            <span className="material-symbols-outlined text-sm" style={{ fontVariationSettings: "'FILL' 1" }}>smart_toy</span>
                        </div>
                    </div>
                )}
                
                <div className="max-w-[85%] flex flex-col gap-2">
                    {msg.category && msg.role === 'bot' && msg.category !== 'GREETING' && (
                        <div className={`self-start px-2 py-0.5 rounded text-[10px] font-label-md font-semibold tracking-wider bg-surface-container border border-outline-variant/30 uppercase ${msg.category === 'ERROR' ? 'text-error' : 'text-secondary'}`}>
                            {msg.category}
                        </div>
                    )}
                    
                    {msg.role === 'user' ? (
                        <div className="bg-primary-container text-on-primary-fixed-variant rounded-2xl rounded-tr-sm px-5 py-4 font-body-md text-body-md shadow-md border border-primary/30">
                            <p>{msg.content}</p>
                        </div>
                    ) : (
                        <div className="glass-panel-active bot-glow rounded-2xl rounded-tl-sm px-5 py-4 text-on-surface font-body-md text-body-md">
                            {renderMessageContent(msg.content)}
                        </div>
                    )}
                </div>
            </div>
          ))}

          {/* Typing Indicator */}
          {isLoading && (
            <div className="flex w-full mb-6 animate-message opacity-0" style={{ animationDelay: '0.1s', animationFillMode: 'forwards' }}>
              <div className="flex-shrink-0 mr-3 mt-1">
                <div className="w-8 h-8 rounded-full bg-surface-container-highest flex items-center justify-center border border-primary/20 text-primary">
                  <span className="material-symbols-outlined text-sm" style={{ fontVariationSettings: "'FILL' 1" }}>smart_toy</span>
                </div>
              </div>
              <div className="max-w-[85%]">
                <div className="glass-panel rounded-2xl rounded-tl-sm px-5 py-4 flex items-center gap-1 h-[52px]">
                  <div className="w-2 h-2 rounded-full bg-primary/60 typing-dot"></div>
                  <div className="w-2 h-2 rounded-full bg-primary/60 typing-dot"></div>
                  <div className="w-2 h-2 rounded-full bg-primary/60 typing-dot"></div>
                </div>
              </div>
            </div>
          )}
          
          <div ref={messagesEndRef} />
        </div>

        {/* Fixed Bottom Input Area */}
        <div className="fixed bottom-0 left-0 w-full z-40 bg-gradient-to-t from-background via-background/90 to-transparent pt-10 pb-6 px-4 md:px-0 flex flex-col items-center">
          <div className="w-full md:w-2/3 lg:w-[60%] flex flex-col gap-4">
            
            {/* Suggestion Chips - Always available above input */}
            {!isLoading && (
                <div className="w-full overflow-x-auto pb-2 -mb-2 scrollbar-hide chip-pop opacity-0" style={{ animationDelay: '0.2s', animationFillMode: 'forwards' }}>
                    <div className="flex gap-2 min-w-max px-1">
                    {exampleQueries.map((q, idx) => (
                        <button 
                            key={idx} 
                            onClick={() => handleSend(q)}
                            className="px-4 py-2 rounded-full glass-panel text-on-surface-variant font-label-md text-label-md hover:bg-primary/10 hover:text-primary hover:border-primary/30 transition-all duration-300 ease-spring active:scale-95 text-xs whitespace-nowrap flex items-center gap-1"
                        >
                            <span className="material-symbols-outlined text-[14px]">bolt</span>
                            {q}
                        </button>
                    ))}
                    </div>
                </div>
            )}

            {/* Input Bar */}
            <div className="relative w-full group">
              <div className="absolute inset-0 bg-primary/5 rounded-2xl blur-md group-focus-within:bg-primary/10 transition-colors duration-300"></div>
              <div className="relative flex items-center bg-surface-container-highest/60 backdrop-blur-3xl border border-outline-variant/30 rounded-2xl px-2 py-2 shadow-2xl focus-within:border-primary/50 focus-within:ring-1 focus-within:ring-primary/50 transition-all duration-300">
                <button className="p-2 text-outline hover:text-primary transition-colors">
                  <span className="material-symbols-outlined">add_circle</span>
                </button>
                <input 
                  autoComplete="off" 
                  className="flex-1 bg-transparent border-none focus:ring-0 text-on-surface placeholder:text-outline-variant font-body-md text-body-md px-2 py-3 outline-none" 
                  placeholder="Ask a factual question about HDFC funds..." 
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleSend(input)}
                  disabled={isLoading}
                />
                <button 
                    onClick={() => handleSend(input)} 
                    disabled={isLoading || !input.trim()}
                    className="bg-primary text-on-primary w-10 h-10 rounded-xl flex items-center justify-center hover:bg-primary-fixed-dim hover:shadow-[0_0_15px_rgba(59,130,246,0.4)] transition-all duration-300 ease-spring active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>send</span>
                </button>
              </div>
            </div>
            
            <div className="text-center md:hidden">
              <span className="font-label-md text-[10px] text-outline-variant">Facts-only. No investment advice.</span>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
