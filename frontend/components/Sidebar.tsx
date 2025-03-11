import Image from 'next/image';
import React from 'react'

interface Conversation {
    id: string;
    name: string;
    userId: string;
}

interface SidebarProps {
    conversations: Conversation[];
}

const Sidebar = ({ conversations }: SidebarProps) => {
    return (
        <div className='admin-sidebar'>
            <div>
                <div className='logo'>
                    <Image 
                            src="/icons/next.svg"
                            alt="logo"
                            height={37}
                            width={37}
                    />
                    <h1 className='logo'>Drop RAG</h1>
                </div>

                <div className='mt-10 flex flex-col gap-5'>
                    {conversations.map((conversation) => (
                        <div 
                                key={conversation.id} 
                                className="conversation-item p-3 rounded-lg hover:bg-gray-100 cursor-pointer"
                        >
                                <p className="font-medium">{conversation.name}</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Sidebar