from datetime import datetime, timedelta
from ryanair import Ryanair
from ryanair.types import Flight

def print_flights_pretty(flights: list[Flight]):
    """Print a nice table-like output of flights."""
    if not flights:
        print("No flights found.")
        return

    print("\n=== Cheapest Flights ===")
    print(f"{'Departure':<20} {'Destination':<10} {'Price':<10} {'Currency':<10}")
    print("-" * 50)

    for f in flights:
        dep = f.departureTime.strftime("%Y-%m-%d %H:%M")
        print(f"{dep:<20} {f.destination:<10} {f.price:<10} {f.currency:<10}")

    print("-" * 50)


def get_n_cheapest_flights(origin: str, date, n: int = 5, currency="CZK"):
    """
    Get N cheapest flights from origin on a specified date.
    """
    api = Ryanair(currency=currency)

    # Ryanair API expects a date range → from `date` to `date + 1 day`
    flights = api.get_cheapest_flights(origin.upper(), date, date + timedelta(days=1))

    # Sort by price (already sorted, but just in case)
    flights = sorted(flights, key=lambda f: f.price)

    # Return N flights
    return flights[:n]


if __name__ == "__main__":
    origin = "VIE"
    date = datetime(2025, 12, 5).date()  # your test date
    number_of_flights = 10

    cheapest = get_n_cheapest_flights(origin, date, number_of_flights, currency="CZK")
    print_flights_pretty(cheapest)

