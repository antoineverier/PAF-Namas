//
//  Language.swift
//  NAMAS
//
//  Created by Antoine Verier on 26/06/2023.
//

import Foundation
struct Data : Identifiable {
    let id = UUID()
    
    let name : String
    let date : String
    let image : String
    
}

extension Data {
    static let list : [Data] = [
        Data( name : "Mariia Baranova", date : "2022-12-23", image : "patient1"),
        Data( name : "Sara Meziane", date : "2023-01-04", image : "patient2"),
        Data( name : "Nina Landry", date : "2021-10-21", image : "patient3"),
        Data( name : "Antoine Verier", date : "2022-02-12", image : "patient4"),
        Data( name : "Paul Dupont", date : "2020-03-03", image : "patient5"),
        Data( name : "Robert Rousseau", date : "2023-10-08", image : "patient6"),
        Data( name : "Louis Chirac", date : "2021-02-14", image : "patient7"),
        Data( name : "François De Saint Exupéry", date : "2022-06-30", image : "patient8"),
        Data( name : "Mireille Mathieu", date : "2020-09-17", image : "patient9"),
        Data( name : "Monique Legendre", date : "2023-11-29", image : "patient10"),]
}
