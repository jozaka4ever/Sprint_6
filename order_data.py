from dataclasses import dataclass


@dataclass(frozen=True)
class OrderData:
    case_id: str
    entry_point: str
    first_name: str
    last_name: str
    address: str
    metro_station: str
    phone: str
    delivery_days_from_today: int
    rental_period: str
    color: str
    comment: str


class OrderTestData:
    CASES = (
        OrderData(
            case_id="top-button-black-scooter",
            entry_point="top",
            first_name="Иван",
            last_name="Иванов",
            address="улица Садовая, дом 7",
            metro_station="Сокольники",
            phone="+79991234567",
            delivery_days_from_today=2,
            rental_period="двое суток",
            color="black",
            comment="Позвонить за час до доставки",
        ),
        OrderData(
            case_id="bottom-button-grey-scooter",
            entry_point="bottom",
            first_name="Мария",
            last_name="Петрова",
            address="улица Лесная, дом 15",
            metro_station="Черкизовская",
            phone="+79997654321",
            delivery_days_from_today=7,
            rental_period="пятеро суток",
            color="grey",
            comment="Оставить у консьержа",
        ),
    )
