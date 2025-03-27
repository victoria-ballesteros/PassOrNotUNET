from typing import List

grade_ranges = [
            # (rango_min, rango_max, nota_base)
            (0, 7, 1.0), (8, 8, 1.1), (9, 9, 1.2), (10, 10, 1.3), (11, 11, 1.4), (12, 12, 1.5), (13, 13, 1.6),(14, 14, 1.7), (15, 15, 1.8), (16, 16, 1.9),
            (17, 18, 2.0), (19, 19, 2.1), (20, 20, 2.2), (21, 21, 2.3), (22, 22, 2.4), (23, 23, 2.5), (24, 24, 2.6), (25, 25, 2.7), (26, 26, 2.8), (27, 27, 2.9),
            (28, 29, 3.0), (30, 30, 3.1), (31, 31, 3.2), (32, 32, 3.3), (33, 33, 3.4), (34, 34, 3.5), (35, 35, 3.6), (36, 36, 3.7), (37, 37, 3.8), (38, 38, 3.9),
            (39, 40, 4.0), (41, 41, 4.1), (42, 42, 4.2), (43, 43, 4.3), (44, 44, 4.4), (45, 45, 4.5), (46, 46, 4.6), (47, 47, 4.7), (48, 49, 4.8), (50, 50, 4.9), 
            (51, 51, 5.0), (52, 52, 5.1), (53, 53, 5.2), (54, 55, 5.3), (56, 56, 5.4), (57, 57, 5.5), (58, 58, 5.6), (59, 59, 5.7), (60, 60, 5.8), (61, 61, 5.9),
            (62, 63, 6.0), (64, 64, 6.1), (65, 65, 6.2), (66, 66, 6.3), (67, 67, 6.4), (68, 68, 6.5), (69, 69, 6.6), (70, 70, 6.7), (71, 71, 6.8), (72, 72, 6.9),
            (73, 74, 7.0), (75, 75, 7.1), (76, 76, 7.2), (77, 77, 7.3), (78, 78, 7.4), (79, 79, 7.5), (80, 80, 7.6), (81, 81, 7.7), (82, 82, 7.8), (83, 83, 7.9),
            (84, 85, 8.0), (86, 86, 8.1), (87, 87, 8.2), (88, 88, 8.3), (89, 89, 8.4), (90, 90, 8.5), (91, 91, 8.6), (92, 92, 8.7), (93, 93, 8.8), (94, 94, 8.9),
            (95, 100, 9.0)  # 95 o más
        ]

class calculatePercentages:
    def __init__(self):
        pass

    def calculate(self, percentages: List[int], scores: List[int]):

        if len(percentages) != len(scores):
            return -1
        for i in range(len(percentages)):
            if (percentages[i] < 0 or scores[i] < 0) or (percentages[i] > 100 or scores[i] > 100):
                return -1
        
        # Calcular porcentaje restante
        percentageToCalculate = 100 - sum(percentages)
        #percentages.append(percentageToCalculate)

        baseScore = []

        for score in scores:
            for rango_min, rango_max, nota_base in grade_ranges:
                if rango_min <= score <= rango_max:
                    baseScore.append(nota_base)
        
        print("Los porcentajes son: ", percentages)
        print("La notas en conversión es: ", baseScore)
        
        
        finalScore = 0.0
        for i in range(len(percentages)):
            finalScore += baseScore[i] * (percentages[i]/100)
   
        print("La nota actual es: ", finalScore)

        _7left = (7-finalScore)/(percentageToCalculate/100)
        _6left = (6-finalScore)/(percentageToCalculate/100)
        _5left = (5-finalScore)/(percentageToCalculate/100)

        print("Falta para el 7: ", _7left)
        print("Falta para el 6: ", _6left)
        print("Falta para el 5: ", _5left)

