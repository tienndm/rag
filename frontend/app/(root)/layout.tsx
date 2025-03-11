import Sidebar from '@/components/Sidebar'
import React, { ReactNode } from 'react'

const Layout = async({children}: {children: ReactNode}) => {
  const dummyInput = [
    {
      "id": "5565b54c7b2a4a70a71a568910d7e589",
      "name": "Xin chào",
      "userId": "aded4bdef9574785b79ad0ab50aed169"
    },
    {
        "id": "5565b54c7b2a4a70a71a568910d7e589",
        "name": "Xin chào 1",
        "userId": "aded4bdef9574785b79ad0ab50aed169"
      }
  ];

  return (
    <main className='flex min-h-screen w-full flex-row'>
        <Sidebar conversations={dummyInput}/>
        <div className='admin-container'>
            <div className='mt-20 pb-20'>
                {children}
            </div>
        </div>
    </main>
  )
}

export default Layout