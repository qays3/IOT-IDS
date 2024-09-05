<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $secretKey = 'c55d47f942c79e312982f60d1a584b46';
    $receivedKey = $_POST['secretkey'] ?? '';

    if ($receivedKey !== $secretKey) {
        http_response_code(403);
        echo json_encode(['message' => 'Unauthorized']);
        exit;
    }

    $to = 'qayssarayra.h@gmail.com';
    $subject = 'Threat Detected';

    $ip = $_POST['ip'] ?? 'N/A';
    $threat_id = $_POST['threat_id'] ?? 'N/A';
    $threat_name = $_POST['threat_name'] ?? 'N/A';

    $message = '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {margin: 0; padding: 0; font-family: \'Source Sans Pro\', Helvetica, Arial, sans-serif; background-color: #1e212a; color: #ffffff;}
        section {max-width: 600px; margin: 20px auto; background-color: #1e212a; border-radius: 10px; overflow: hidden; text-align: center; color: #ffffff;}
        div {padding: 24px; font-size: 16px; line-height: 24px;}
        a {display: inline-block; padding: 16px 36px; font-size: 16px; color: #ffffff; text-decoration: none; background-color: #6f42c1; border-radius: 6px;}
    </style>
</head>
<body>

    <section>
        <div>
            <h1 style="margin: 0; font-size: 32px; font-weight: 700; letter-spacing: -1px; line-height: 48px;">Threat Detected!</h1>
        </div>

        <div>
            <p style="margin: 0;">A potential threat has been detected with the following details:</p>
            <p><strong>IP Address:</strong> ' . htmlspecialchars($ip) . '</p>
            <p><strong>Threat ID:</strong> ' . htmlspecialchars($threat_id) . '</p>
            <p><strong>Threat Name:</strong> ' . htmlspecialchars($threat_name) . '</p>
        </div>
        
        <div>
            <a href="https://metaitcoding.com" target="_blank" style="color: white;">View Threat Details</a>
        </div>

        <div>
            <p style="margin: 0;">Please review the threat and take appropriate action.</p>
        </div>
    </section>

    <section>
        <div>
            <p style="font-size: 14px; line-height: 20px; margin: 0;">You received this email from CyberAlien\'s threat detection system.</p>
        </div>
    </section>

</body>
</html>';

    $headers = [
        'MIME-Version' => '1.0',
        'Content-Type' => 'text/html; charset=UTF-8'
    ];

    $headersString = '';
    foreach ($headers as $key => $value) {
        $headersString .= "$key: $value\r\n";
    }

    if (mail($to, $subject, $message, $headersString)) {
        echo json_encode(['message' => 'Notification sent']);
    } else {
        http_response_code(500);
        echo json_encode(['message' => 'Failed to send notification']);
    }
} else {
    http_response_code(405);
    echo json_encode(['message' => 'Method Not Allowed']);
}
?>
