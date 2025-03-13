import ChatContent from '@/components/ChatContent'
import ChatInput from '@/components/ChatInput'
import { getChats } from '@/lib/actions/chat'
import React from 'react'

const page = async ({params}: {params: {id: string}}) => {
    const {id} = params
    const chats = await getChats({conversationsId: id})
    
  return (
    <div className="flex flex-col h-screen max-h-screen overflow-hidden">
      <div className="flex-1 overflow-y-auto">
        <ChatContent chatContent={chats}/>
      </div>
        <div className="border-t border-gray-200 p-4 bg-white">
            <ChatInput conversationId={id} />
        </div>
    </div>
  )
}

export default page