def city_country(city, country, population=None, language=None):
    """Return a formatted city and country with optional population and language."""

    result = f"{city}, {country}"

    if population is not None:
        result += f" - population {population}"

    if language is not None:
        result += f", {language}"

    return result


print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France", 2161000))
print(city_country("Tokyo", "Japan", 13960000, "Japanese"))
