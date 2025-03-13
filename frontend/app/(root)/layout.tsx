import Sidebar from '@/components/Sidebar'
import { getConversations } from '@/lib/actions/chat'
import React, { ReactNode } from 'react'

const Layout = async({children}: {children: ReactNode}) => {
  const userId = 'aded4bdef9574785b79ad0ab50aed169'
  const conversations = await getConversations({userId})

  return (
    <main className='flex min-h-screen w-full flex-row'>
        <Sidebar conversations={conversations}/>
        <div className='admin-container'>
            <div className='mt-20 pb-20'>
                {children}
            </div>
        </div>
    </main>
  )
}

export default Layout