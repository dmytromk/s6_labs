package com.aircompany.servlets;

import com.aircompany.db.dao.*;
import com.aircompany.db.entity.*;
import com.aircompany.parsers.JsonParser;
import com.aircompany.servlets.util.RequestPack;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.BufferedReader;
import java.io.IOException;
import java.sql.Connection;
import java.util.ArrayList;
import java.util.List;

@WebServlet("/request")
public class RequestServlet extends HttpServlet {

    public void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    }
}
