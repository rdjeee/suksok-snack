import type { Metadata, Viewport } from "next";
import { Plus_Jakarta_Sans, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";

/**
 * Plus Jakarta Sans — heading & body font (spec §3.1)
 * Modern, clean, friendly — cocok untuk brand "Moring" yang ramah.
 */
const plusJakarta = Plus_Jakarta_Sans({
  variable: "--font-plus-jakarta",
  subsets: ["latin"],
  display: "swap",
  weight: ["400", "500", "600", "700", "800"],
});

/**
 * JetBrains Mono — numeric/monospace untuk harga, order code, no resi (spec §3.3)
 * Tabular figures untuk alignment angka.
 */
const jetbrainsMono = JetBrains_Mono({
  variable: "--font-jetbrains-mono",
  subsets: ["latin"],
  display: "swap",
  weight: ["400", "500", "600"],
});

export const metadata: Metadata = {
  title: {
    default: "Suksok Snack — Camilan Cimol Kering (Moring) 🌿",
    template: "%s — Suksok Snack",
  },
  description:
    "Suksok Snack: cimol kering (moring) sehat & renyah. Belanja online mudah, bayar QRIS, lacak pesanan real-time. UMKM lokal Indonesia.",
  keywords: [
    "Suksok Snack",
    "cimol kering moring",
    "moringa",
    "snack sehat",
    "UMKM Indonesia",
    "moring cimol kering",
    "belanja online",
    "QRIS",
  ],
  authors: [{ name: "Suksok Snack" }],
  creator: "Suksok Snack",
  publisher: "Suksok Snack",
  icons: {
    icon: [
      { url: "/favicon.ico", sizes: "any" },
      { url: "/icon.svg", type: "image/svg+xml" },
    ],
    apple: "/icon-apple.png",
  },
  manifest: "/manifest.json",
  openGraph: {
    title: "Suksok Snack — Snack Sehat dari Alam",
    description: "Cimol kering (moring) sehat & renyah. Belanja online, bayar QRIS, lacak pesanan.",
    siteName: "Suksok Snack",
    locale: "id_ID",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Suksok Snack — Snack Sehat dari Alam",
    description: "Cimol kering (moring) sehat & renyah. Belanja online, bayar QRIS, lacak pesanan.",
  },
};

export const viewport: Viewport = {
  themeColor: "#2D6A4F",
  width: "device-width",
  initialScale: 1,
  maximumScale: 5,
  userScalable: true,
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="id" suppressHydrationWarning>
      <body
        className={`${plusJakarta.variable} ${jetbrainsMono.variable} font-sans antialiased`}
      >
        {children}
        <Toaster />
      </body>
    </html>
  );
}
