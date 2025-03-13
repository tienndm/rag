import { Input } from './ui/input';
import { Button } from './ui/button';
import Image from 'next/image';
import React from 'react'

interface ChatInputProps {
    conversationsId: string;
}


const ChatInput = ({conversationId}: ChatInputProps) => {
  return (
    <div className='flex flex-col gap-4 px-4 py-6 w-[70%] mx-auto'>
        <div className="relative w-full">
            <Input 
                type="text" 
                placeholder="Ask anything" 
                className="text-xl pr-10 py-6" 
            />
            <Button 
                type="submit" 
                className="absolute right-1 top-1/2 transform -translate-y-1/2 h-10 w-10 p-0" 
                aria-label="Send"
            >
                <Image 
                    src='/icons/send.svg'
                    alt='send'
                    width={24}
                    height={24}
                />
            </Button>
        </div>
    </div>
  )
}

export default ChatInput