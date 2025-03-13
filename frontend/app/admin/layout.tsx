import React, { ReactNode } from 'react'

const layout = async ({children}: {children: ReactNode}) => {
  return (
    <main>
        <div>
            {children}
        </div>
    </main>
  )
}

export default layout