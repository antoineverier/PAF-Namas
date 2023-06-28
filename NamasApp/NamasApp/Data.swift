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
        Data( name : "Nina Landry", date : "2021-10-21", image : "patient3"),]
}
