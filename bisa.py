import asyncio
from telethon import TelegramClient

# =========================
# KONFIGURASI
# =========================

API_ID = 39924866
API_HASH = "71383f6f5029c593a880a7dcdb1eee5a"

SESSION = "akun_1"
TARGET = "@obrolan_app"

PESAN = [
    "Halo ce",
    "@kiyaraisaa",
    "/next"
]

JEDA = 10
MAKS_PUTARAN = 1000


# =========================
# PROGRAM UTAMA
# =========================

async def main():
    print("=" * 35)
    print("   TELEGRAM MESSAGE TEST")
    print("=" * 35)

    async with TelegramClient(
        SESSION,
        API_ID,
        API_HASH
    ) as client:

        akun = await client.get_me()

        print(f"Akun aktif: {akun.first_name}")
        print(f"Target: {TARGET}")
        print(f"Pesan per putaran: {len(PESAN)}")
        print(f"Jumlah putaran: {MAKS_PUTARAN}")
        print(f"Jeda: {JEDA} detik")

        konfirmasi = input(
            "\nKetik KIRIM untuk memulai: "
        ).strip()

        if konfirmasi != "KIRIM":
            print("Pengiriman dibatalkan.")
            return

        for putaran in range(1, MAKS_PUTARAN + 1):
            print(f"\n=== PUTARAN {putaran} ===")

            for nomor, pesan in enumerate(PESAN, start=1):
                try:
                    await client.send_message(
                        TARGET,
                        pesan
                    )

                    print(
                        f"[BERHASIL] "
                        f"Putaran {putaran}, "
                        f"pesan {nomor}: {pesan}"
                    )

                    if (
                        nomor < len(PESAN)
                        or putaran < MAKS_PUTARAN
                    ):
                        await asyncio.sleep(JEDA)

                except Exception as error:
                    print(f"[GAGAL] {error}")
                    return

        print("\nPengujian selesai.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram dihentikan.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")