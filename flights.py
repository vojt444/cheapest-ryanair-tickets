from datetime import datetime, timedelta
from ryanair import Ryanair
from ryanair.types import Flight
from tabulate import tabulate


def print_flights_pretty(flights: list[Flight]):
    if not flights:
        print("No flights found.")
        return

    table = []
    for f in flights:
        table.append(
            [
                f.departureTime.strftime("%Y-%m-%d %H:%M"),
                f.destinationFull,
                f.flightNumber,
                f"{f.price:.0f}",
                f.currency,
            ]
        )

    print("\n=== Cheapest Flights ===")
    print(
        tabulate(
            table,
            headers=["Departure", "Destination", "Flight No.", "Price", "Currency"],
            tablefmt="fancy_grid",
        )
    )


def get_n_cheapest_flights(origin: str, date, n: int = 5, currency="CZK"):
    """
    Get N cheapest flights from origin on a specified date.
    """
    api = Ryanair(currency=currency)

    # Ryanair API expects a date range → from `date` to `date + 1 day`
    flights = api.get_cheapest_flights(origin.upper(), date, date + timedelta(days=0))

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
