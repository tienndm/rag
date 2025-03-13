"use client"
import { cn } from '@/lib/utils';
import Image from 'next/image';
import Link from 'next/link'
import { usePathname } from 'next/navigation';
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
    const pathname = usePathname();
    return (
        <section className='sidebar'>
            <nav className='flex flex-col gap-4'>
                <Link 
                    href='/' 
                    className="mb-12 cursor-pointer flex items-center gap-2"
                >
                    <Image 
                        src="/icons/next.svg"
                        alt="logo"
                        width={34}
                        height={34}
                    />
                    <h1 className='sidebar-logo'>Drop Rag</h1>
                </Link>

                {conversations.map((conversation) => {
                    const isActive = pathname === `/chat/${conversation.id}` || pathname.startsWith(`/chat/${conversation.id}`)
                    return (
                        <Link 
                            href={`/chat/${conversation.id}`} 
                            key={conversation.id} 
                            className={cn('sidebar-link', {'bg-bank-gradient': isActive})}
                        >
                            <p className={cn('sidebar-label', {'!text-white': isActive})}>
                                {conversation.name}
                            </p>
                        </Link>
                    )
                })}
            </nav>
        </section>
    )
}

export default Sidebar