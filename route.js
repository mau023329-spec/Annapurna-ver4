// app/api/auth/[...nextauth]/route.js
import NextAuth from "next-auth"
import GoogleProvider from "next-auth/providers/google"

export const authOptions = {
  providers: [
    GoogleProvider({
      clientId:     process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    }),
  ],
  pages: {
    signIn: "/login",
  },
  callbacks: {
    async session({ session, token }) {
      if (session?.user) {
        session.user.id = token.sub
      }
      return session
    },
    async jwt({ token }) {
      return token
    },
    // FIX: previously this always returned baseUrl + "/onboarding" for any
    // OAuth redirect, so returning users were always bounced to /onboarding
    // after login. Now we send to /login and let login/page.jsx decide
    // whether to go to /chat (returning user) or /onboarding (new user)
    // based on whether preferences are already saved.
    async redirect({ url, baseUrl }) {
      if (url.startsWith(baseUrl)) return url
      return baseUrl + "/login"
    },
  },
  secret: process.env.NEXTAUTH_SECRET,
}

const handler = NextAuth(authOptions)
export { handler as GET, handler as POST }
