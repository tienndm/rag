import React from 'react'
import { Avatar } from './ui/avatar'


interface ChatContent {
    id: number;
    chatRole: number;
    conversationId: string;
    messages: string;
}

interface ChatContentProps {
    chatContent: ChatContent[];
}

const ChatContent = ({chatContent}: ChatContentProps) => {
  if (!chatContent || chatContent.length === 0) {
    return <div className="flex justify-center items-center h-full">No messages yet</div>
  }

  return (
    <div className="flex flex-col gap-4 px-4 py-6 w-[70%] mx-auto">
        {chatContent.map((chat) => (
            <div 
                key={chat.id}
                className={`flex gap-3 ${chat.chatRole === 1 ? 'justify-end' : 'justify-start'}`}
            >
                {chat.chatRole === 2 && (
                    <Avatar className="h-8 w-8">
                        <span className="font-semibold text-xs">AI</span>
                    </Avatar>
                )}
                
                <div 
                    className={`max-w-[80%] p-3 rounded-lg ${
                        chat.chatRole === 1 
                            ? 'bg-primary text-primary-foreground' 
                            : 'bg-muted'
                    }`}
                >
                    {chat.messages}
                </div>
                
                {chat.chatRole === 1 && (
                    <Avatar className="h-8 w-8">
                        <span className="font-semibold text-xs">TN</span>
                    </Avatar>
                )}
            </div>
        ))}

        
    </div>
  )
}

export default ChatContent